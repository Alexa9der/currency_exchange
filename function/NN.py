from import_libraries.libraries import  *

# feature optimizer
class GradientRFE:
    def __init__(self, data):
        self.data = data
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None
        self.best_rmse = float('inf')
        self.best_parameters = None

    def prepare_data(self, window_size=25, y_column="Close_diff", test_size=0.2):
        # Drop the target column before scaling
        data_for_scaling = self.data.drop(y_column, axis=1)

        # Split data into training and test sets
        train_size = int(len(self.data) * (1 - test_size))
        train_data = data_for_scaling.iloc[:train_size]
        test_data = data_for_scaling.iloc[train_size:]

        # Initialize and fit MinMaxScaler on the training data
        scaler = MinMaxScaler(feature_range=(0, 1))
        train_scaled = scaler.fit_transform(train_data)

        # Transform both training and test sets using the trained scaler
        train_scaled = scaler.transform(train_data)
        test_scaled = scaler.transform(test_data)

        X_train, y_train = self.__create_sequences(train_scaled, window_size, y_column)
        X_test, y_test = self.__create_sequences(test_scaled, window_size, y_column)

        self.X_train, self.y_train = X_train, y_train
        self.X_test, self.y_test = X_test, y_test

        return self.X_train, self.y_train, self.X_test, self.y_test

    
    def model_LSTM(self, shape: list[int, int]):
        input_layer = Input(shape = shape )

        # додать keras-tuner !!!
        lstm_layer = LSTM(64, activation='relu', return_sequences=True)(input_layer)
        flatten_layer = Flatten()(lstm_layer)
        output_layer = Dense(1, activation='linear')(flatten_layer)

        model = Model(inputs=input_layer, outputs=output_layer)

        self.model = model
        
        return self.model

            
    def fit(self, num_features_to_keep=5, window_size=25, epochs=10):
        
        X_train, y_train, X_test, y_test = self.prepare_data()
        index_of_min_value = []
        for count in tqdm(range(self.X_train.shape[2] - num_features_to_keep)):           
            
            model = clone_model(self.model_LSTM( shape=[X_train.shape[1], X_train.shape[2]]))
            model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mean_absolute_error'])
    
            # Обучение модели на текущих данных
            model.fit(X_train, y_train, epochs=epochs, verbose=0)

            # Оценка модели на тестовых данных после обучения
            y_pred_before = model.predict(X_test)
            mse_before = mean_squared_error(y_test, y_pred_before)
            rmse_before = np.sqrt(mse_before)
            mape_before = np.mean(np.abs((y_test - y_pred_before) / y_test)) * 100
            
            # Получение градиентов относительно входных данных
            with tf.GradientTape() as tape:
                inputs = tf.convert_to_tensor(X_train)
                tape.watch(inputs)
                predictions = model(inputs)
                loss = tf.reduce_mean(tf.square(predictions - y_train))
            
            gradients = tape.gradient(loss, inputs)
            
            # Рассчет абсолютных значений градиентов
            absolute_gradients = np.abs(gradients.numpy())
            
            # Усреднение важностей признаков
            average_importance = np.mean(absolute_gradients, axis=0)
            # print(average_importance.shape)
            
            # Преобразование глобального индекса в индекс по временным шагам
            index_of_min_value_global = np.argmin(average_importance)
            index_of_min_value_time = index_of_min_value_global % X_train.shape[2]
            # print(index_of_min_value_time)
            
            # Удаляем признак с наименьшим весом из данных
            X_train = np.delete(X_train, index_of_min_value_time, axis=2)
            X_test = np.delete(X_test, index_of_min_value_time, axis=2)
            
    
            # Обновление модели
            model = clone_model(self.model_LSTM([X_train.shape[1], X_train.shape[2]] ))
            model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mean_absolute_error'])
            
            # Обучение модели на новых данных
            model.fit(X_train, y_train, epochs=epochs, verbose=0)
    
            # Оценка модели на тестовых данных после обучения
            y_pred_after = model.predict(X_test)
            mse_after = mean_squared_error(y_test, y_pred_after)
            rmse_after = np.sqrt(mse_after)
            mape_after = np.mean(np.abs((y_test - y_pred_after) / y_test)) * 100
    
            print(f"Test MSE before training: {mse_before}.\nTest RMSE before training: {rmse_before}.")
            print(f"Test MAPE before training: {mape_before}%")
            print(f"Test MSE after training: {mse_after}.\nTest RMSE after training: {rmse_after}.")
            print(f"Test MAPE after training: {mape_after}%")
            
            index_of_min_value.append(index_of_min_value_time + count)
            self.__best_result(num_features_to_keep, index_of_min_value, rmse_before, rmse_after)

    def __create_sequences(self, data, window_size, y_column):
        X, y = [], []

        for i in range(len(data) - window_size):
            window = data[i:(i + window_size)]
            X.append(window)
            y.append(self.data.loc[i + window_size, y_column])

        return np.array(X), np.array(y)

    def __best_result(self, num_features_to_keep, index_of_min_value, rmse_before, rmse_after):
        if rmse_after < self.best_rmse:
            self.best_rmse = rmse_after
            num_features = [i for i in range(self.X_train.shape[2]) if i not in index_of_min_value]
            self.best_parameters = {
                "best number of features": len(num_features),
                'best_rmse': self.best_rmse,
                'num_features_to_keep': num_features,
                'index_of_min_value': index_of_min_value,
            }





























