import sqlite3 

class funkopop2: 

    def _connect_(self): 
        #function connects the user to the funko pop databse provided 
        #in github profile 
        
        print('You are now connecting to the ' + self.dbpath + '.') 
        self.conn = sqlite3.connect(self.dbpath)
        print ('welcome') 

    def create_table_region(self):
        #creates table for regions 
        #attributes: 

        try:  #try = if 
            self.conn.execute ('''CREATE TABLE region (


                                              )''')

        except sqlite3.OperationalError: 
            print('Table already exists')
        pass

    def main(self): 