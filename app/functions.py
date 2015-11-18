from app import mysql

# Returns array of dictionary objects based on query
def get_result(query, values):
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute(query, values)
	data = []
	row = row_to_dict(cursor)
	
	while row is not None:
		data.append(row)
		row = row_to_dict(cursor)

	cursor.close() 
	conn.close()
	return data


def row_to_dict(cursor):
	data = cursor.fetchone()
	desc = cursor.description
	if data is None:
		return None
	dict = {}
	for (name, value) in zip(desc, data):
		dict[name[0]] = value
	return dict


