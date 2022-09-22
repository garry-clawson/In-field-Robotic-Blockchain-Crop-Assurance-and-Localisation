
import requests
import base64

# ======= request CID hash from user ============

def request_cid():

    CID = input("Enter your CID: ")
    return CID

# ======= get image from IPFS ============

def get_image(hash):
 
    params = (
    ('arg', hash),
    )

    response = requests.post('https://ipfs.infura.io:5001/api/v0/cat', params=params)
    image_file = response.text
    #print(response.text) #base64 text for image

    #convert from base64 to image and write to directory
    image_64_decode = base64.b64decode(image_file)  
    image_result = open('returned_template_ground_stone_plan_view.jpeg', 'wb') # create a writable image and write the decoding result
    image_result.write(image_64_decode)

# ========== Entry point to script ========

def main():
    hash = request_cid()
    get_image(hash)


if __name__ == "__main__":
    main()
