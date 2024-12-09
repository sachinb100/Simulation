class DatabaseRouter:
    def db_for_read(self,model,**hints):
        if model._meta.app_label=='multitask':
            if model.__name__=='User':
                return 'users_db'
            elif model.__name__=='Order':
                return 'orders_db'
            elif model.__name__=='Product':
                return 'products_db'
        return None

    def db_for_write(self,model,**hints):
        if model._meta.app_label=='multitask':
            if model.__name__ == 'User':
                return 'users_db'
            elif model.__name__=='Order':
                return 'orders_db'
            elif model.__name__=='Product':
                return 'products_db'
        return None
