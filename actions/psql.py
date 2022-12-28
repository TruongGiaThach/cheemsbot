import psycopg2
from underthesea import pos_tag

def create_connection():
	""" create a database connection to a postgreSQL database """
	#postgres://cheemsdb_user:5WeyXPGknSQwhMoVf8imVgzodUzVoyN5@dpg-cdhv15mn6mpue9hhnk8g-a.singapore-postgres.render.com/cheemsdb
	conn = None
	try:
		conn = psycopg2.connect(user='postgres', password='123456', host='127.0.0.1', port='5432', database='cheemstore')
	except (Exception, psycopg2.Error) as e:
		print(e)
	return conn

def get_info_from_cate(_cate):
	conn = create_connection()
	try:

		cur = conn.cursor()

		sql = """ SELECT P.name
	              FROM products as P, product_categories as PC
	              WHERE P.product_category = PC.id and 
				  lower(PC.name) like %s
	          """
		_cate = "'%" + _cate + "%'"
		print(_cate)
		cur.execute(sql,(_cate,))
		conn.commit()
		records = cur.fetchall()
		return records
	except:
		conn.rollback()

# def get_info_gv_from_mon_hoc(subjects):
# 	conn = create_connection()
# 	try:
# 		cur = conn.cursor()
# 		sql = """ SELECT GiaoVien.TenGiaoVien
# 					FROM HocPhan
# 					join GiaoVien_HocPhan on GiaoVien_HocPhan.MaHocPhan = HocPhan.MaHocPhan
# 					join GiaoVien on GiaoVien_HocPhan.MaGiaoVien = GiaoVien.MaGiaoVien 
# 					WHERE HocPhan.TenHocPhan ilike %s
# 	          """
# 		cur.execute(sql, (subjects,))
# 		conn.commit()
# 		records = cur.fetchall()
# 		return records
# 	except:
# 		conn.rollback()


# def get_list_subject():
# 	conn = create_connection()
# 	try:
# 		cur = conn.cursor()
# 		sql = """ SELECT tenhocphan
# 					FROM hocphan
# 	          """
# 		cur.execute(sql)
# 		conn.commit()
# 		records = cur.fetchall()
# 		return records
# 	except:
# 		conn.rollback()

# def get_info_student(student_code):
	# conn = create_connection()
	# try:
	# 	cur = conn.cursor()
	# 	sql = """ select hocphan.tenhocphan, score.score from score 
	# 				join hocphan on score.mahocphan = hocphan.mahocphan
	# 			  where score.masinhvien= %s
	#           """
	# 	cur.execute(sql, (student_code,))
	# 	conn.commit()
	# 	records = cur.fetchall()
	# 	return records
	# except:
	# 	conn.rollback()

# if __name__ == '__main__':
# 	record = get_info_gv_from_mon_hoc('%t%o%á%n%r%ờ%i%r%ạ%c%')
#
# 	sr = ', '.join([', '.join(i) for i in record])
# 	text = "Môn học " +
# 	print(sr)
# print(get_list_subject())get_list_store


def get_info_store():
	conn = create_connection()
	try:
		cur = conn.cursor()
		sql = """ SELECT name
					FROM product_categories
	          """
		cur.execute(sql)
		conn.commit()
		records = cur.fetchall()
		return records
	except:
		conn.rollback()