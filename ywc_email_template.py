def build_body(body: str) -> str:
    return f"""
    <div style="font-family: Tahoma, sans-serif;">
        <div>
            {body}
        </div>
        <div>
            <p>-----</p>
            <img 
                style="width: 120px;"
                src="https://raw.githubusercontent.com/WebmasterCamp/bulk-emails-ywc19/main/assets/ywc19-colored-logo-with-bg.png"
            />
            <p>
                Young Webmaster Camp, in associate with Thai Webmaster and Online Media Association.<br />
                ติดตามข่าวได้ที่ Facebook <a href="https://www.facebook.com/ywcth" target="_blank">YoungWebmaster Camp</a>
                | Instagram <a href="https://www.instagram.com/ywcth/" target="_blank">@ywcth</a> 
                | Twitter <a href="https://twitter.com/ywcth" target="_blank">@ywcth</a>
            </p>
        </div>
    </div>
    """


def build_camper_acceptance_letter_email(
    camper_title: str,
    camper_fullname: str,
    camper_major: str,
) -> str:
    body = f"""
    <p>เรียน {camper_title}{camper_fullname}<br/>
    <br/>
    ตามที่{camper_title}{camper_fullname} ได้รับการคัดเลือกให้เข้าร่วมโครงการอบรมเชิงปฏิบัติการ <b>"ก้าวสู่วิชาชีพเว็บมาสเตอร์"</b> 
    หรือ <b>Young Webmaster Camp ครั้งที่ 19</b> 
    ในสาขา Web {camper_major} โดยโครงการฯ มีกำหนดจัดขึ้นระหว่างวันที่ 14 - 17 กรกฎาคม พ.ศ. 2566 
    ณ ศูนย์ฝึกอบรมธนาคารไทยพาณิชย์ หาดตะวันรอน ต.นาจอมเทียน อ.สัตหีบ จ.ชลบุรี 
    ทางคณะดำเนินงานฯ ขอนำส่งหนังสือรับรองการคัดเลือกเข้าร่วมโครงการฯ แนบมากับอีเมลฉบับนี้<br/>
    <br/>
    เพื่อเป็นการยืนยันว่าคุณได้รับอีเมลฉบับนี้แล้ว โปรดตอบกลับหาเรา (Reply) ว่า "ได้รับเรียบร้อย"<br/>
    <br/>
    หากมีข้อสงสัยประการใด สามารถสอบถามได้ที่ นายจักภัท มิ่งมงคลมิตร (ประธานโครงการ) หมายเลขโทรศัพท์ 098-919-2919<br/>
    <br/>
    จึงเรียนมาเพื่อทราบ<br/>
    นายจักภัท มิ่งมงคลมิตร<br/>
    ประธานโครงการฯ
    </p>
    """
    return build_body(body)
