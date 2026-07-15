# Hướng dẫn chỉnh sửa nội dung website LêVănThông Education

Tài liệu này dành cho nhân viên **không rành kỹ thuật** — chỉ cần biết dùng máy tính cơ bản. Làm theo đúng thứ tự các bước, không cần hiểu code.

---

## 1. Cài công cụ chỉnh sửa (chỉ làm 1 lần)

1. Tải **Visual Studio Code** (miễn phí) tại: https://code.visualstudio.com → chọn bản cho Mac hoặc Windows → cài như phần mềm bình thường.
2. Mở VS Code → **File** → **Open Folder** → chọn thư mục:
   `Website_Trung tam luyen thi` (thư mục chứa toàn bộ website).
3. Bên trái màn hình sẽ hiện danh sách file — đây là nơi bạn sẽ làm việc mỗi lần sửa nội dung.

---

## 2. Bản đồ file — trang nào nằm ở đâu

| Muốn sửa trang... | Mở file... |
|---|---|
| Trang chủ | `index.html` |
| Khóa Toán | `programs/toan.html` |
| Khóa Vật lý | `programs/vatly.html` |
| Khóa Anh văn | `programs/anhvan.html` |
| Giới thiệu Thầy Lê Văn Thông | `about.html` |
| Phương pháp học | `method.html` |
| Lịch khai giảng | `schedule.html` |
| Form đăng ký tư vấn | `assessment.html` |
| Kết quả học viên | `results.html` |
| Thông tin công khai (giấy phép...) | `public-info.html` |
| Liên hệ | `contact.html` |

Mỗi file `.html` là **một trang riêng biệt**. Sửa file nào thì chỉ trang đó thay đổi — trừ menu và chân trang (xem mục 5).

---

## 3. Cách sửa văn bản trên trang

### Quy tắc vàng — đọc kỹ trước khi sửa
- **Chỉ sửa chữ nằm giữa dấu `>` và `<`.** Ví dụ dòng này:
  ```html
  <h1 class="text-3xl font-bold text-[--color-primary]">Khóa Vật lý (Lớp 6–12)</h1>
  ```
  Bạn **chỉ được sửa** phần `Khóa Vật lý (Lớp 6–12)`, **không đụng vào** phần `<h1 class="...">` hay `</h1>`.
- **Không xóa dấu `<`, `>`, `"`** — xóa nhầm sẽ làm hỏng cả trang.
- Sau khi sửa xong, **nhấn ⌘S (Mac) hoặc Ctrl+S (Windows) để lưu.**
- Nếu không chắc, **copy nguyên dòng ra một file Word/Notes trước khi sửa** để có bản gốc phòng khi cần khôi phục.

### Ví dụ 1 — Đổi số điện thoại
Trong VS Code, nhấn **⌘F / Ctrl+F** để tìm, gõ `0919222595`, sẽ thấy nhiều dòng dạng:
```html
<a href="tel:0919222595" class="...">📞 Gọi ngay</a>
```
Đổi số ở cả 2 chỗ: trong `tel:...` (không dấu cách) và bất kỳ chỗ nào hiển thị số có định dạng `0919 222 595`.
**Lưu ý:** số điện thoại xuất hiện ở **tất cả các trang** (menu, chân trang), nên phải tìm-và-thay ở từng file, hoặc dùng chức năng **Tìm & Thay trong toàn bộ dự án**: nhấn **⌘⇧F (Mac) / Ctrl+Shift+F (Windows)** → gõ số cũ vào ô tìm, số mới vào ô thay → bấm **Replace All**.

### Ví dụ 2 — Đổi học phí
Mở `programs/toan.html` (hoặc vatly.html, anhvan.html), tìm chữ `1.500.000đ`, sẽ thấy:
```html
<p class="text-gray-600 mt-1">1.500.000đ/tháng (1 buổi/tuần). Học 2-3 buổi/tuần: mức giá thương lượng, liên hệ trung tâm để được tư vấn</p>
```
Sửa trực tiếp phần chữ, giữ nguyên thẻ `<p class="...">` và `</p>`.
**Lưu ý:** học phí xuất hiện ở **3 file** `toan.html`, `vatly.html`, `anhvan.html` và cả trong `schedule.html` — sửa đủ cả 4 file để đồng bộ.

### Ví dụ 3 — Sửa cảm nhận học viên (testimonial)
Mở `index.html`, tìm chữ `Học viên nói gì`, kéo xuống sẽ thấy các dòng dạng:
```html
<div class="bg-white border rounded-xl p-5 text-sm text-gray-600">"Nội dung cảm nhận..."<p class="mt-2 font-semibold text-gray-800">— Phụ huynh học sinh</p></div>
```
Sửa phần chữ trong dấu `"..."` (câu cảm nhận) và phần sau dấu `—` (tên/vai trò người nói). Testimonial còn có ở `about.html` và `results.html`.

### Ví dụ 4 — Sửa tiêu đề trang (SEO, hiện trên tab trình duyệt)
Đầu mỗi file có dòng:
```html
<title>Trang chủ | LêVănThông Education</title>
<meta name="description" content="...">
```
Có thể sửa cả hai, nhưng giữ nguyên cấu trúc `<title>...</title>` và `content="..."`.

---

## 4. Cách thêm / thay hình ảnh

### Bước 1 — Chuẩn bị ảnh
- Định dạng: **.jpg** hoặc **.png**.
- Kích thước khuyến nghị: rộng khoảng **1200px**, dung lượng dưới **500KB** (ảnh quá nặng làm web tải chậm). Có thể dùng trang https://squoosh.app (miễn phí) để nén ảnh trước khi upload.
- Đặt tên file **không dấu, không khoảng trắng**, dùng gạch ngang. Ví dụ: `hoc-vien-toan-lop-9.jpg` (không đặt tên `Ảnh mới 1.jpg`).

### Bước 2 — Copy ảnh vào đúng thư mục
Trong VS Code (hoặc Finder/File Explorer), copy file ảnh vào thư mục:
```
assets/images/
```
Tất cả ảnh hiện có cũng nằm ở đây: `teacher-whiteboard.jpg`, `classroom-group.jpg`, `student-english-study.jpg`.

### Bước 3 — Chèn ảnh vào trang
Mở file HTML của trang cần thêm ảnh, tìm vị trí muốn chèn, thêm dòng:
```html
<img src="/assets/images/ten-file-anh.jpg" alt="Mô tả ngắn về ảnh" class="rounded-xl w-full h-auto object-cover aspect-video">
```
- `src="/assets/images/ten-file-anh.jpg"` — **đúng tên file** vừa copy vào bước 2.
- `alt="..."` — mô tả ngắn bằng tiếng Việt (giúp SEO và người khiếm thị), ví dụ `alt="Học viên lớp 9 trong giờ học Toán"`.
- Phần `class="..."` giữ nguyên để ảnh hiển thị đẹp, bo góc, responsive trên điện thoại.

### Bước 4 — Thay ảnh cũ bằng ảnh mới
Tìm dòng `<img src="/assets/images/...">` đang có, đổi phần tên file trong `src=` sang tên ảnh mới đã copy vào `assets/images/`.

---

## 5. Sửa menu / chân trang (áp dụng cho TẤT CẢ các trang)

Menu (header) và chân trang (footer) được **lặp lại giống hệt nhau** trên mọi trang — nghĩa là sửa 1 chỗ thì phải sửa **thủ công ở từng file**, vì trang web này không dùng "khung chung" tự động.

**Cách hiệu quả nhất:** dùng **⌘⇧F / Ctrl+Shift+F** (tìm trong toàn bộ dự án) → tìm đoạn chữ cần đổi → **Replace All** để sửa cùng lúc ở tất cả các trang. Ví dụ: đổi tên trung tâm, đổi địa chỉ, đổi giờ hoạt động.

⚠️ Nếu thấy không tự tin khi sửa nhiều file cùng lúc, hãy nhờ người có kinh nghiệm kỹ thuật hỗ trợ hoặc liên hệ tôi (Claude) qua phiên làm việc mới.

---

## 6. Xem thử trước khi đưa lên web thật

Trước khi public, **luôn xem thử trên máy** để chắc chắn không bị lỗi:

1. Mở **Terminal** (Mac) → gõ:
   ```bash
   cd "/Users/lehongtran/Desktop/Website_Trung tam luyen thi"
   python3 -m http.server 8000
   ```
2. Mở trình duyệt, vào địa chỉ: `http://localhost:8000`
3. Kiểm tra trang vừa sửa — chữ hiển thị đúng không, ảnh có hiện không, có bị vỡ giao diện không.
4. Xong việc, quay lại Terminal, nhấn **Ctrl+C** để tắt server thử nghiệm.

---

## 7. Đưa thay đổi lên website thật (levanthongedu.com)

Website đang dùng **Git + GitHub + Netlify**: mỗi khi đẩy thay đổi lên GitHub, Netlify sẽ **tự động cập nhật** website thật trong khoảng 1 phút.

Sau khi đã lưu file và xem thử ổn (mục 6), mở **Terminal**, gõ lần lượt:
```bash
cd "/Users/lehongtran/Desktop/Website_Trung tam luyen thi"
git add .
git commit -m "Cập nhật nội dung: mô tả ngắn gọn thay đổi vừa làm"
git push
```
Thay `"Cập nhật nội dung: ..."` bằng mô tả thật, ví dụ `"Cập nhật học phí khóa Toán"` hoặc `"Thêm ảnh học viên mới"`.

Sau khoảng 1 phút, mở `https://levanthongedu.com` để kiểm tra thay đổi đã lên web thật chưa.

---

## 8. Checklist trước khi công bố nội dung mới

- [ ] Đã lưu file (⌘S / Ctrl+S)
- [ ] Đã xem thử trên `localhost:8000`, không thấy lỗi hiển thị
- [ ] Ảnh mới đã nén, đặt tên đúng chuẩn (không dấu, không khoảng trắng)
- [ ] Nếu sửa thông tin xuất hiện nhiều trang (SĐT, học phí, địa chỉ...), đã sửa **đủ tất cả các file** liên quan
- [ ] Đã chạy `git add . && git commit -m "..." && git push`
- [ ] Đã mở `levanthongedu.com` kiểm tra lại sau khi push

---

## 9. Lỗi thường gặp

| Hiện tượng | Nguyên nhân thường gặp | Cách khắc phục |
|---|---|---|
| Trang trắng xóa hoặc vỡ giao diện | Xóa nhầm dấu `<`, `>`, hoặc dấu `"` | Mở lại file, so sánh với bản gốc đã backup, hoặc chạy `git checkout -- ten-file.html` để khôi phục về bản đã lưu gần nhất trên Git |
| Ảnh không hiện | Sai tên file trong `src=`, hoặc ảnh chưa copy vào `assets/images/` | Kiểm tra tên file trong `src=` khớp chính xác (kể cả hoa/thường) với tên file trong thư mục |
| Push lên GitHub báo lỗi | Chưa đăng nhập, hoặc mất kết nối mạng | Chạy `gh auth status` để kiểm tra đăng nhập, hoặc thử lại `git push` |
| Sửa xong nhưng web thật chưa đổi | Netlify build lỗi, hoặc mới push chưa đủ 1 phút | Đợi thêm 1-2 phút, hoặc vào Netlify dashboard xem log build có lỗi không |

---

## 10. Việc KHÔNG nên tự làm (cần người kỹ thuật hỗ trợ)

- Thêm trang mới hoàn toàn (cần tạo file mới đúng cấu trúc menu/chân trang)
- Sửa cấu trúc bảng, form, hoặc bất kỳ đoạn code JavaScript nào (file `js/main.js`)
- Đổi cấu hình DNS, domain, hosting (Cloudflare, Netlify)
- Tích hợp Google Sheets, reCAPTCHA, Google Analytics, Facebook Pixel — các phần này chưa được kích hoạt (xem `README.md`)

Với các việc trên, hãy liên hệ người phụ trách kỹ thuật hoặc mở lại phiên làm việc với Claude Code.
