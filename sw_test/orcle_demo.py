import cx_Oracle
import re
db_connection=cx_Oracle.connect('testuser/testpass@XXXXXXX:XXXX/service_name')

cursor=db_connection.cursor()

sql='SELECT * FROM mespro.INV_SOCIALRET_MACHINE where inv_org_id=200788'
cursor.execute(sql)

result=cursor.fetchall()
# for item in result:
#     print(item)

result=str(result)


pattern = '\), \('
result = re.sub(pattern,"')\n('",result)
print(result)
#
#
# result=result.replace('(','\n(')
#
# print(result)

# phone = "2004-959-559 # 这是一个电话号码"
# num = re.sub('\D', "", phone)
# print ("电话号码 : ", num)
#
# cursor.close()
# db_connection.close()