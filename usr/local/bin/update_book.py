import http.client
import json

def read_db():

    conn = http.client.HTTPConnection('morned270.dothome.co.kr')

    conn.request('POST','/readBookExpired.php')

    response = conn.getresponse()
    json_str = response.read().decode()
    try:
        json_data = json.loads(json_str)
        print(json_data['webnautes'])

        for i in json_data['webnautes']:
            print (i['user_num'])
            user_num = i['user_num']
            update_db(user_num)
    except:
        print('nothing expired')


    conn.close()

def update_db(user_num):

    conn = http.client.HTTPConnection('morned270.dothome.co.kr')

    postParameters = str(user_num)

    byte_array = postParameters.encode()
    conn.request('POST','/cancelBookExpired.php',byte_array)

    response = conn.getresponse()
    print(response.read().decode())

    conn.close()

if __name__=="__main__":
    # update_db(1, "50")
    read_db()