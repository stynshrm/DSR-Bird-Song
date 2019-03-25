from birdsong.data_management.management import DatabaseManager

dbm = DatabaseManager('storage')

#dbm.clean_db()

dbm.make_selection(100, 1000)
dbm.download_missing()



t, v, codes = dbm.train_validation_split()

import pandas as pd
c = pd.DataFrame.from_dict(codes, orient='index').reset_index()
c= c.rename(columns={'index':'code', 0:'name'})

t.path = t.path.apply(lambda x: x.replace('.pkl', '.png'))
v.path = v.path.apply(lambda x: x.replace('.pkl', '.png'))

t.to_csv('top100_img_train.csv')
v.to_csv('top100_img_val.csv')
c.to_csv('top100_img_codes.csv')
