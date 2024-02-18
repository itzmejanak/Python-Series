import requests
import re
import sys
import os
from Crypto.Cipher import AES
import shutil
import asyncio
import aiohttp
import json
import time
from Crypto.Util.Padding import unpad

with open('done.json','r',encoding="utf-8") as f: 
    alrdydone=json.load(f)

plid="16355" # "4764" 
plname=""
if plname:
    plname=" - "+plname

headerz={"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNTUzMDI2YzUzNjQ1ODM1YTRmNDUzNTk1MjM3NWYxZGVhYWU1NjI1YmQxZjljZmViMjkzNjA0YjU1NTNjNjU0OWEwYmY3ZTg0NjE0Y2RmMzQiLCJpYXQiOjE2OTcxMTY1ODguNDIxOTA0LCJuYmYiOjE2OTcxMTY1ODguNDIxOTA3LCJleHAiOjE3MjgyMjA1ODguNDE3OTY3LCJzdWIiOiI4NTE2MCIsInNjb3BlcyI6WyJjdXN0b21lcnMiXX0.LyUryYlknM_jABE4arLA6cF2XwHzckq6bBV5lTsOyrCFhptxkCCva7QdBHk-CFvKL4BcqWdf7HvWuleQT64eHo-jlXeakNEezZEVScHNMqHVfnoY8yBEZXCt9j0s0jQPrtKxBAkupAvZSEKo5UWyzBWK6xhUTw8w1TC4LpeGZ4FxemUcp2HBXAmdgIG4yYMJJqHu4uXya6Q7IZSEcRIi0QexNST3LvSOzzOuuMPo0AzW4GpvufR8zZBJrQwSCjS6zKwPnByQFkA3PYzK93cyRQRiGPlJUdPYlAcOxJ2MrO_0INyoBm-S25fCb39e7uSiFopHNgeKbQnG2RSlBiK8qsjlWQ7YNN9nUwMYILBcl9FcWXBzAsFi5e_F6sQ2quWhq-PtTAQ5mvO4pxKSqSePOnRN-Xy540n0XwyM-MnXPYrY1931nR62INaFYuUtSDDKXYjY_zYhQhIaM7QM-BCH6k4_u_jQWDDE7MCZlKu4ax3TLTYv--J7o6hkpWtnzNnNfNA3FT2Rdf-Qnn3gj8ojOeYLiK27ZwAXHGBeex8-41Xdu0JtiCtPd_6BCGt6eQl5l75Xq-Yhpse2DIefasvDOT4fqYrU8IzFEX9l3PmQYckxAZRaM7Pc6eAcTBAYbd-3BjYppLK2cknDJpdHWPzdpjQn0ekyDf4QLxwmUnd3VV0","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.2109.1","Fingerprint":"2097581312","Content-Type":"application/json"}

headers={"X-Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNTUzMDI2YzUzNjQ1ODM1YTRmNDUzNTk1MjM3NWYxZGVhYWU1NjI1YmQxZjljZmViMjkzNjA0YjU1NTNjNjU0OWEwYmY3ZTg0NjE0Y2RmMzQiLCJpYXQiOjE2OTcxMTY1ODguNDIxOTA0LCJuYmYiOjE2OTcxMTY1ODguNDIxOTA3LCJleHAiOjE3MjgyMjA1ODguNDE3OTY3LCJzdWIiOiI4NTE2MCIsInNjb3BlcyI6WyJjdXN0b21lcnMiXX0.LyUryYlknM_jABE4arLA6cF2XwHzckq6bBV5lTsOyrCFhptxkCCva7QdBHk-CFvKL4BcqWdf7HvWuleQT64eHo-jlXeakNEezZEVScHNMqHVfnoY8yBEZXCt9j0s0jQPrtKxBAkupAvZSEKo5UWyzBWK6xhUTw8w1TC4LpeGZ4FxemUcp2HBXAmdgIG4yYMJJqHu4uXya6Q7IZSEcRIi0QexNST3LvSOzzOuuMPo0AzW4GpvufR8zZBJrQwSCjS6zKwPnByQFkA3PYzK93cyRQRiGPlJUdPYlAcOxJ2MrO_0INyoBm-S25fCb39e7uSiFopHNgeKbQnG2RSlBiK8qsjlWQ7YNN9nUwMYILBcl9FcWXBzAsFi5e_F6sQ2quWhq-PtTAQ5mvO4pxKSqSePOnRN-Xy540n0XwyM-MnXPYrY1931nR62INaFYuUtSDDKXYjY_zYhQhIaM7QM-BCH6k4_u_jQWDDE7MCZlKu4ax3TLTYv--J7o6hkpWtnzNnNfNA3FT2Rdf-Qnn3gj8ojOeYLiK27ZwAXHGBeex8-41Xdu0JtiCtPd_6BCGt6eQl5l75Xq-Yhpse2DIefasvDOT4fqYrU8IzFEX9l3PmQYckxAZRaM7Pc6eAcTBAYbd-3BjYppLK2cknDJpdHWPzdpjQn0ekyDf4QLxwmUnd3VV0","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.2109.1","Fingerprint":"2097581312"}
    
def decrypt(data, key, iv):
    try:
        decryptor = AES.new(key, AES.MODE_CBC, IV=iv)
        decrypted_data = decryptor.decrypt(data)
        # Unpad the decrypted data using PKCS7
        unpadded_data = unpad(decrypted_data, AES.block_size)
        return unpadded_data
    except ValueError as ve:
        print(f"Decryption error: {ve}")
        return b''  # Return an empty bytes-like object in case of decryption failure
    except Exception as e:
        print(f"Unexpected error during decryption: {e}")
        return b''  # Return an empty bytes-like object in case of decryption failure


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            # data = await response.content.read()
            # return data
            async for chunk in response.content.iter_any():  # Use iter_any() to iterate over chunks
                yield chunk
            

async def get_binary(url):
    data = b''
    while True:
        try:
            async for chunk in fetch_data(url):
                data += chunk
            break
        except:
            time.sleep(5)
            print('err0')
            pass
    return data

async def doit(key_url,iv_val,data_url,cnt,vid):
    key = await get_binary(key_url)
    enc_data = await get_binary(data_url)

    dec_data = decrypt(enc_data, key, iv_val)
    # if not dec_data: return

    with open(f'{vid}/{cnt}.ts', 'wb') as f:
        f.write(dec_data)

async def main(vid,tit):
    print(f'Downloading {vid}...')

    m3url=f"https://api.ambition.guru/api/web/customer/content-video/playlist/{vid}/VIDEOS_{vid}.m3u8"
    while True:
        try:
            r=requests.get(m3url,headers=headers)
            break
        except:
            time.sleep(5)
            print('err1')
            pass
    # if r.status_code!=200:
        # print('skipped----------------------------------------')
        # return
    m3u8rl=r.text.split('\n')[-2].strip('')
    while True:
        try:
            rr=requests.get(m3u8rl,headers=headers)
            break
        except:
            print('err2')
            time.sleep(5)

    keys=re.findall('https://api.ambition.guru/api/web/customer/video/key/(.*?).key',rr.text)

    datas=re.findall('https://cdn.ambition.guru/agvideostream/medias/videos/.*',rr.text)

    ivs=re.findall('.key",IV=0x(.*)',rr.text)

    total=len(ivs)

    if not os.path.exists(vid):
        os.makedirs(vid)

    i=0
    for iv in ivs:
        i+=1
        print(f'{i}/{total}')
        if os.path.exists(f'{vid}/{i+1}.ts'): continue
        await doit(f'https://api.ambition.guru/api/web/customer/video/key/{keys[i-1]}.key',bytes.fromhex(iv),datas[i-1],i,vid)
                
    print('Combining..')
    try:
        with open(f'out/{vid} _ {tit}{plname}.ts', 'wb') as merged:
            i=0
            for ts_file in ivs:
                i+=1
                if not os.path.exists(f'{vid}/{i}.ts'): continue
                with open(f'{vid}/{i}.ts', 'rb') as mergefile:
                    shutil.copyfileobj(mergefile, merged)
    except:
        tit=re.sub(r"[^\w]", " ", tit)
        with open(f'out/{vid} _ {tit}{plname}.ts', 'wb') as merged:
            i=0
            for ts_file in ivs:
                i+=1
                if not os.path.exists(f'{vid}/{i}.ts'): continue
                with open(f'{vid}/{i}.ts', 'rb') as mergefile:
                    shutil.copyfileobj(mergefile, merged)
        
    shutil.rmtree(vid)
    with open('done.json','r',encoding="utf-8") as f: 
        alrdydone=json.load(f)    
    alrdydone['ids'].append(vid)
    with open('done.json',"w",encoding="utf-8") as f:
        f.write(json.dumps(alrdydone))

for i in range(1,100):
    while True:
        try:
            pl=requests.post("https://api.ambition.guru/api/web/customer/get-contents-by-section?page="+str(i),headers=headerz, data=json.dumps({"type": "UNIT", "id": plid, "content_type": "VIDEOS", "page": i, "display_type": "all"})).json()
            break
        except:
            print('err3')
            time.sleep(5)
    tot=pl["data"]["meta"]["total"]
    cur=pl["data"]["meta"]["to"]
    print('#########################################')
    print(f'{cur}/{tot}')
    vids=pl["data"]["data"]
    for v in vids:
        vid=str(v["id"])
        if vid in alrdydone['ids']: continue
        # if vid in ['10936']: continue
        print('****************************************')
        tit=v["title"]
        print(tit)
        # skip=input(f"Skip? {vid}: {tit}: (y) ")
        # if skip=='y':
            # with open('done.json','r',encoding="utf-8") as f: 
                # alrdydone=json.load(f)        
            # alrdydone['ids'].append(vid)
            # with open('done.json',"w",encoding="utf-8") as f:
                # f.write(json.dumps(alrdydone))                
            # continue
        while True:
            try:
                getimg=requests.get(v["thumbnail"]["path"])
                break
            except:
                print(getimg.text)
                print(getimg.headers)
                time.sleep(5)
                print('err4')
                pass                    
        with open(f'out/{vid}.jpg', 'wb') as f:
            f.write(getimg.content)
            
        asyncio.run(main(vid,tit))
    if tot==cur: break
    
print('done')