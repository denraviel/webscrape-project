from bs4 import BeautifulSoup as BS
import requests
import pymysql.cursors

url = "https://www.jumia.com.ng/mlp-adidas-store/"
headers = requests.utils.default_headers()
headers.update({
   "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
})

Brand_name_list=[]
Brand_description1 =[]
old_price1 =[]
new_price1 =[]
category1 =[]
for x in range (1,37):
    my_response = requests.get(f"https://www.jumia.com.ng/mlp-adidas-store/?page={x}#catalog-listing")
    # print(my_response.status_code)
    first_soup = BS(my_response.content, features = "lxml")
    soup2 = first_soup.find("div", attrs={"class":"-paxs row _no-g _4cl-3cm-shs"})
        # print(soup2)

    list_soups = soup2.find_all("article", attrs = {"class":"prd _fb col c-prd"})
    

    for soup in list_soups:
        
        Addidas_Jumia_details = soup.find ("a")
        try:
        
            brandname = Addidas_Jumia_details.get("data-brand")
            # print(brandname)
        except:
            brandname = None
            

            
            




               

       

        try:
            brand_detailed_description = Addidas_Jumia_details.get("data-name")
            # print(game_detailed_description)
             
                
        except:
            brand_detailed_description = None
        
        

        try:
            category = Addidas_Jumia_details.get("data-category")
            if "/" in category:
                categoryy = (category).split("/")[0]
                # print(categoryy)
                
        except:
            categoryy = None




        try:
            old_div = soup.find("div", attrs = {"class" : "old"})
            old_price = int((old_div.text).lstrip("₦").replace(",", ""))
                # print(sneakers_old_price)
        except:
            old_price = None
       

        try: 
            new_div = soup.find("div", attrs = {"class" : "prc"})
            new_price = int((new_div.text).lstrip("₦").replace(",", ""))
                # print(phone_new_price)

        except:
#             new_price = None
        
        
         Brand_name_list.append(brandname)
      

         Brand_description1.append(brand_detailed_description)
         category1.append(categoryy) 
         old_price1.append(old_price)
         new_price1.append(new_price)
         
         zippedd =zip(Brand_name_list,Brand_description1,category1,old_price1,new_price1)
         zipped_list = list(zippedd)
         print(zipped_list)
      


          
       




connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='jumiaAddidasMerch',
                             cursorclass=pymysql.cursors.DictCursor)

# def create_customer_table():
#     with connection:
        
#         with connection.cursor() as cursor:
        
#             sql = "CREATE TABLE product(id INT(10)AUTO_INCREMENT PRIMARY KEY NOT NULL,BrandName CHAR(50),Branddesc VARCHAR(600),Category VARCHAR(120),OldPrice INT(7),NewPrice INT(7));"
#             cursor.execute(sql)
#             connection.commit()
# # create_customer_table()                


# def insert_into_product_uno():
#       with connection.cursor() as cursor:

#           for items in zipped_list:
            # sql = "INSERT INTO product (Brandname,Branddesc,Category,OldPrice,Newprice) VALUES('{}','{}','{}','{}','{}')".format(*items)
#             cursor.execute(sql)
#             connection.commit()
# insert_into_product_uno()

def find_p():
   df= input("details:")
   
   with connection.cursor() as cursor:
      
        
      sql = "SELECT * FROM product WHERE Branddesc LIKE ('{}')".format(df)
      cursor.execute(sql)
      result=cursor.fetchall()
      connection.commit()   
      print(result)
find_p()


