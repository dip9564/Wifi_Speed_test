import streamlit as st
import speedtest 

st.header("🛜 NetWork Speed Test")
st.markdown("Must on InterNet or cunnected Wifi")

if st.button("Run"):
    try:
        sp = speedtest.Speedtest()

        with st.spinner("Testing Speed..."):
            sp.get_best_server()

            st.info("its take some time")
            download_speed = sp.download() / 1_000_000
            upload_speed = sp.upload() / 1_000_000
            ping_result = sp.results.ping

            speed={
                'download': round(download_speed, 2),
                'upload': round(upload_speed, 2),
                'ping': ping_result
            }
            st.success(f"⬇️ Download Speed : {speed['download']} Mbps")
            st.success(f"⬆️ Upload Speed   : {speed['upload']} Mbps")
            st.success(f"🛜 Ping           : {speed['ping']:.2f} ms")
    except Exception as e:
        st.error(f"check netWork connection{e}")
