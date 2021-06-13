from mysql import connector


class ConnectionFactory:
    @staticmethod
    def get_connection():
        return connector.connect(
                    host="localhost",
                    user="yourusername",
                    password="yourpassword"
                )


if __name__ == '__main__':
    ConnectionFactory().get_connection()
