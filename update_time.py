import http.client

def update_db(uses_num, left_time):

    conn = http.client.HTTPConnection('morned270.dothome.co.kr')

    postParameters = str(uses_num)+","+left_time

    byte_array = postParameters.encode()
    conn.request('POST','/updateTime.php',byte_array)

    response = conn.getresponse()
    print(response.read().decode())

    conn.close()

if __name__=="__main__":
    update_db(1, "50")