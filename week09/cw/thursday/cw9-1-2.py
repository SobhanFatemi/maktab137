class NoConnectionError(Exception):
    pass

class ConnectionPool:
    def __init__(self, size):
        self.size = size
        self.available_connections = [f"connection{i+1}" for i in range(size)]
        self.in_use_connection=[]
        self.current_connection= None

    def __enter__(self):
        if not self.available_connections:
            raise NoConnectionError("No available connections")
        self.current_connection = self.available_connections.pop(0)
        self.in_use_connection.append(self.current_connection)
        return self.current_connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.current_connection:
            self.in_use_connection.remove(self.current_connection)
            self.available_connections.append(self.current_connection)
            self.current_connection = None

#Usage
if __name__ == "__main__":
    pool = ConnectionPool(size=1)

    try:
        with pool as conn1:
            print(conn1)

            with pool as conn2:
                print(conn2)

                with pool as conn3:
                    print(conn3)

    except NoConnectionError as e:
        print(e)