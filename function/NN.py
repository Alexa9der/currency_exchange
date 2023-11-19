# feature optimizer
class GradientRFE:
    def __init__(self, data):
        self.data = data
        self.X = None
        self.y = None
        self.best_mse = float('inf')
        self.best_parameters = None

    def prepare_data(self, window_size=25, y_column="close"):
        X, y = [], []
    
        for i in range(len(self.data) - window_size):
            window = self.data.iloc[i:(i + window_size)].drop(y_column, axis=1)
            X.append(window.values)
            y.append(self.data.loc[i + window_size, y_column])
    
        self.X = np.array(X)
        self.y = np.array(y)
    
        return self.X, self.y

    
    def model_LSTM(self, shape: list[int, int]):
        input_layer = Input(shape = shape )

        # додать keras-tuner !!!
        lstm_layer = LSTM(64, activation='relu', return_sequences=True)(input_layer)
        flatten_layer = Flatten()(lstm_layer)
        output_layer = Dense(1, activation='linear')(flatten_layer)

        model = Model(inputs=input_layer, outputs=output_layer)

        self.model = model
        
        return self.model

    
    def __best_result(self, num_features_to_keep, index_of_min_value, mse_before, mse_after):
        if mse_after < self.best_mse:
            self.best_mse = mse_after
            num_features = [i for i in range(self.X.shape[2]) if i not in index_of_min_value]
            self.best_parameters = {
                "best number of features": len(num_features),
                'best_mse': self.best_mse,
                'num_features_to_keep': num_features,
                'index_of_min_value': index_of_min_value,
            }
        
            
    def fit(self, num_features_to_keep=5, X=None, y=None, window_size=25, epochs=10):
        
        if not X and not y:
            self.prepare_data(window_size)
        else:
            self.X = X
            self.y = y

    
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        index_of_min_value = []
        
        for count in tqdm(range(self.X.shape[2] - num_features_to_keep)):
            
            model = clone_model(self.model_LSTM( shape=[X_train.shape[1], X_train.shape[2]]))
            model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mean_absolute_error'])
    
            # Обучение модели на текущих данных
            model.fit(X_train, y_train, epochs=epochs, verbose=0)

            # Оценка модели на тестовых данных после обучения
            y_pred_before = model.predict(X_test)
            mse_before = mean_squared_error(y_test, y_pred_before)
            
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
    
            print(f"Removed feature at index {index_of_min_value_time + count}.")
            print(f"Test MSE before training: {mse_before}.\nTest MSE after training: {mse_after}")
            
            index_of_min_value.append(index_of_min_value_time + count)
            self.__best_result(num_features_to_keep, index_of_min_value, mse_before, mse_after)

































