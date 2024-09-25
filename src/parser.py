import sys
import xml.dom.minidom
import mysql.connector

#building connection to database and cursor 
connection = mysql.connector.connect(
    host="localhost",
    user="ghxlam",
    password="123456",
    database="Dunder_Mifflin"
)
cursor = connection.cursor()

filename = sys.argv[1] # reads the filename so we can determine if its a staples or quill file
print("\n\nThe length of the filename is: \n\n", len(filename))
#-8 for s1 s2 q1 q2 and -9 for s11 s12 s13 q11 q12 q13
if(len(filename) == 19 ) :
    filenamestrip = filename[-8:]
else:
    filenamestrip = filename[-9:]

if filenamestrip[0] == "/" :
    filenamestrip = filenamestrip[1]
filenamestrip = filenamestrip[:-6]

print("\n\nThe filename is: \n\n", filenamestrip)

if filenamestrip.startswith("s") : 
    #for staples xhtml files only
    #passing the file to the parser so we can extract
    doc = xml.dom.minidom.parse(sys.argv[1])
    txt = doc.getElementsByTagName("script")[0]
    val = txt.firstChild.nodeValue
    
    #extracting the product name
    pn_si = val.find('name":') + len('"name":')
    pn_ei = val.find('","ima', pn_si + 1)
    pn = val[pn_si:pn_ei]
    
    #extracting the description
    descii = doc.getElementsByTagName("script")[7]
    desctxt = descii.firstChild.nodeValue
    desc_si = desctxt.find('"description":{"paragraph":["') + len('"description":{"paragraph":["')
    desc_ei = desctxt.find('"],"bu', desc_si + 1)
    desc = desctxt[desc_si:desc_ei]
    
    #extracting the product price
    pp_si = val.find('price":') + len('price":')
    pp_ei = val.find(',"price', pp_si)
    pp = val[pp_si:pp_ei]
    pp_num = float(pp)
    
    #extracting the image URL
    iurl_si = val.find('image":[') + len('"image":[')
    iurl_ei = val.find('"],', iurl_si)
    iurl = val[iurl_si:iurl_ei]
    
    #extracting the rating value
    rv_si = val.find('ratingValue":"') + len('ratingValue":"')
    rv_ei = val.find('","review', rv_si)
    rv = val[rv_si:rv_ei]
    
    print("\n\nThe Product Name is: \n\n",pn)
    print("\n\nThe Description is: \n\n", desc)
    print("\n\nThe Price is: \n\n", pp_num)
    print("\n\nThe Image URL is: \n\n", iurl)
    print("\n\nThe Rating is: \n\n", rv)
    
    query = "INSERT INTO Products (fname, product_name, product_description, product_price, image_url, review_score) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (filenamestrip, pn, desc, pp_num, iurl, rv)
    cursor.execute(query, values)
    connection.commit()
else :
    #for quill xhtml files only 
    #parse the xml into minidom
    doc = xml.dom.minidom.parse(sys.argv[1])
    
    #extracting the product name
    title = doc.getElementsByTagName("title")[0]
    titleval = title.firstChild.nodeValue
    titlevalue = titleval[:-12] # gets rid of the quill.com tag at the end of every single quill product name
    
    #extracting the product description
    desc = doc.getElementsByTagName("div")
    descriptionVal = ""
    for element in desc :
        if element.getAttribute("id") == "skuDescription" :
            elems = element.getElementsByTagName("div")
            for elem in elems :
                if "text-left text-justify mb-3" in elem.getAttribute("class") :
                    descriptions = elem.getElementsByTagName("span")
                    for description in descriptions :
                        for childNode in description.childNodes :
                            if childNode.nodeType == childNode.TEXT_NODE : #checks if the node has text or not
                                descriptionVal = childNode.nodeValue
    
    #extracting the product's price
    docElems = doc.getElementsByTagName("script")
    priceVal = ""
    priceValNum = 0
    for element in docElems :
        if element.getAttribute("id") == "SEOSchemaJson" :
            line = element.firstChild.nodeValue
            price_si = line.find('[{"price":') + len('[{"price":')
            price_ei = line.find(',"priceCurr', price_si)
            priceVal = line[price_si:price_ei]
            priceValNum = float(priceVal)
            break
    
    #extracting image url
    img = doc.getElementsByTagName("img")[1]
    imgval = img.getAttribute("src")
    imgvalue = imgval[:-5]
    
    #extract the rating score
    docElems = doc.getElementsByTagName("script")
    ratingVal = ""
    for element in docElems :
        if element.getAttribute("id") == "SEOSchemaJson" :
            line = element.firstChild.nodeValue
            rating_si = line.find('"ratingValue":') + len('"ratingValue":')
            rating_ei = line.find(',"reviewCount', rating_si)
            ratingVal = line[rating_si:rating_ei]
            break
    
    query = "INSERT INTO Products (fname, product_name, product_description, product_price, image_url, review_score) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (filenamestrip, titlevalue, descriptionVal, priceValNum, imgvalue, ratingVal)
    cursor.execute(query, values)
    connection.commit()
    
    print("\n\nThe Product Name is: \n\n",titlevalue)
    print("\n\nThe Description is: \n\n", descriptionVal)
    print("\n\nThe Price is: \n\n", priceValNum)
    print("\n\nThe Image URL is: \n\n", imgvalue)
    print("\n\nThe Rating is: \n\n", ratingVal)
    

#closing the connections to the SQL databases
cursor.close()
connection.close()
