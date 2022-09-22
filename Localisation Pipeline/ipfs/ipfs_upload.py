
import requests
import base64

# ======= push image to IPFS ============

def push_image():

    #convert to base64
    image = open('template_ground_stone_plan_view.jpeg', 'rb')
    image_read = image.read()
    image_64_encode = base64.b64encode(image_read)

    #create file for IPFS
    files = {
    'file': image_64_encode
    }

    #submit to IPFS through infura API
    response = requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files)

    #Get CID has for later use
    p = response.json()
    hash = p['Hash']
    CID = hash
    return CID


# ========== Entry point to script ========

def main():
    hash = push_image()
    print(hash)


if __name__ == "__main__":
    main()