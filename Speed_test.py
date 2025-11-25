import speedtest
def test_speed():
    st=speedtest.Speedtest()

    print("Testing Speed...")

    download_speed=st.download()/1_000_000
    upload_speed=st.upload()/1_000_000
    ping_result=st.results.ping
    return{
        'download':round(download_speed,2),
        'upload':round(upload_speed,2),
        'ping':ping_result
    }
if __name__ == "__main__":
    speed=test_speed()
    print(f"⬇️ Download Speed : {speed['download']} Mbps")
    print(f"⬆️ Upload Speed   : {speed['upload']} Mbps")
    print(f"🛜 Ping           : {speed['ping']:0.2f} ms")