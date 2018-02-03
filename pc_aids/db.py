import psycopg2


class PgSQL:
    def __repr__(self):
        return repr(self.get_cursor())

    def __init__(self, set_manager):
        self.settings = set_manager.get("postgres")

        self.host = self.settings['host']
        self.port = self.settings['port']
        self.user = self.settings['user']
        self.pw = self.settings['pw']
        self.db = self.settings['db']

        self.is_threaded = set_manager.get("global")['threading']

        self.conn = None
        self.cur = None
        self.f_tid = None

        if self.is_threaded:
            self.conn = {}
            self.cur = {}

            import threading
            self.f_tid = threading.get_ident

    def get_connection(self):
        conn = psycopg2.connect(
            "host={c.host}, port={c.port}, user={c.user}, password={c.pw}, dbname={c.db}".format(c=self)
        )

        conn.autocommit = True

        return conn

    def get_cursor(self):
        if not self.is_threaded:
            if self.conn is None or self.conn.closed:
                self.conn = self.get_connection()
                self.cur = self.conn.cursor()

            if self.cur is None:
                self.cur = self.conn.cursor()

            return self.cur

        else:
            tid = self.f_tid()

            if tid not in self.conn.keys():
                self.conn[tid] = self.get_connection()

            if tid not in self.cur.keys():
                self.cur[tid] = self.conn[tid].cursor()

            return self.cur[tid]
