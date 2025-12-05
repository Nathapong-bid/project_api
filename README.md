# Vocabulary Practice API Workshop

FastAPI + MySQL + Docker — Template สำหรับสร้าง REST API + Database สำหรับแอป Vocabulary Practice  

## 🎯 Why / What is this

โปรเจกต์นี้ถูกออกแบบมาเพื่อเป็นโครงฐาน (boilerplate) สำหรับ:

- สร้าง RESTful API ด้วย FastAPI + SQLAlchemy + MySQL + Docker Compose  
- เก็บคำศัพท์และประวัติการฝึก (practice history) ในฐานข้อมูล  
- เชื่อมต่อกับ frontend / mobile / client ได้ง่าย — เหมาะสำหรับโปรเจกต์ฝึกภาษา, vocabulary drill, writing practice  

---

## 📂 Project Structure

project_api/
├─ api/ # โค้ด FastAPI + SQLAlchemy
├─ init.sql # สร้าง Database / Tables / Sample Data
├─ docker-compose.yml # รัน API + MySQL ด้วย Docker
├─ .gitignore
└─ README.md # เอกสารโปรเจกต์


> โฟลเดอร์ `api/` คือส่วน backend หลักที่ใช้พัฒนา API  

---

## 🚀 Quick Start

### สิ่งที่ต้องเตรียม

- Docker + Docker Compose  
- Git  

### เริ่มใช้งาน  

```bash
git clone https://github.com/zhiwei-chen-bu/project_api.git
cd project_api
docker-compose up -d


Docker จะสร้าง container MySQL + API

รัน init.sql เพื่อสร้างตาราง + ข้อมูลเริ่มต้น

เริ่ม server ของ FastAPI

หลังจากนั้นเปิด browser ที่:

http://localhost:8000/docs


เพื่อดูและทดสอบ API ผ่าน Swagger UI

📡 API Endpoints (ตัวอย่าง)
Method	Endpoint	Description
GET	/	ข้อมูล general / list endpoints
GET	/api/word	ดึงคำศัพท์แบบสุ่ม (random word)
POST	/api/validate-sentence	ส่งประโยค → ตรวจ + ให้ feedback/score
GET	/api/summary	สถิติการฝึก (summary)
GET	/api/history	ประวัติการฝึกทั้งหมด (history)
GET	/health	Health check / status of API

ดูรายละเอียด request / response ได้จาก Swagger UI (/docs)

🗄️ Database Schema (โดยสังเขป)
Table: words

id — INT, primary key

word — คำศัพท์ (unique)

definition — ความหมาย / คำอธิบาย

difficulty_level — ระดับ: Beginner / Intermediate / Advanced

created_at — timestamp

Table: practice_sessions

id — INT, primary key

word_id — foreign key → words.id

user_sentence — ประโยคที่ผู้ใช้ส่ง

score — คะแนน (e.g. 0.0–10.0)

feedback — ข้อเสนอแนะ / comment

corrected_sentence — ถ้าระบบแก้ประโยคให้

practiced_at — timestamp

ความสัมพันธ์: หนึ่งคำศัพท์ (word) — หลายประวัติการฝึก (practice_sessions)

🧪 Usage Examples
ดึงคำศัพท์ (Random Word)
curl http://localhost:8000/api/word


ตัวอย่าง response:

{
  "id": 1,
  "word": "apple",
  "definition": "A round fruit with red, green, or yellow skin",
  "difficulty_level": "Beginner"
}

ส่งประโยคเพื่อตรวจสอบ (Validate Sentence)
curl -X POST http://localhost:8000/api/validate-sentence \
  -H "Content-Type: application/json" \
  -d '{
    "word_id": 1,
    "sentence": "I eat an apple every morning for breakfast"
  }'


ตัวอย่าง response:

{
  "score": 8.5,
  "level": "Beginner",
  "suggestion": "Excellent! Your sentence is well-structured.",
  "corrected_sentence": "I eat an apple every morning for breakfast"
}

🛠️ Development & Docker Management

ดูสถานะ containers:

docker ps


หยุด:

docker-compose down


Restart:

docker-compose restart


ลบ volumes + start ใหม่:

docker-compose down -v
docker-compose up -d


เข้า MySQL CLI (ถ้าต้องการจัดการ DB / ตรวจสอบข้อมูล):

docker exec -it <mysql_container_name> mysql -u <user> -p<password> <database_name>

✅ Contributing & Extensions (แนวทางพัฒนาเพิ่มเติม)

เปลี่ยนจากระบบ mock → ใช้ AI จริง เช่น เชื่อมกับ OpenAI API เพื่อให้คะแนน/feedback/แก้ประโยคจริง

ระบบ gamification (streak, leaderboard, achievements)

รองรับผู้ใช้หลายคน (multi-user) + authentication / authorization

Frontend / Mobile client (React, Next.js, Flutter, …) เชื่อม API นี้เพื่อทำ UI/UX

เพิ่มคำศัพท์ / เพิ่มฐานข้อมูลคำศัพท์ (expand word list)

📄 License

ระบุ license ของโปรเจกต์ (เช่น MIT / Apache / GPL) — ถ้ามี

📬 Contact / Feedback

ถ้าพบ bug, มีข้อเสนอแนะ, อยากพัฒนาเพิ่มเติม ฯลฯ — ยินดีต้อนรับ pull request / issues / discussions

Enjoy building — Happy coding!


---

ถ้าคุณอยาก — ผมช่วย **merge** README เวอร์ชันไทย + อังกฤษ (bilingual) ให้เลย เผื่อโปรเจกต์คุณอาจมีคนทั้งไทยและต่างประเทศใช้ — ถ้ามีไฟล์ `.env.example` หรือ config ใด ๆ ให้ผมรู้ด้วย เดี๋ยวเผื่อใส่ลงไปให้ครบ 👍
::contentReference[oaicite:5]{index=5}
