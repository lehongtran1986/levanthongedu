# Website LêVănThông Education

Luyện thi đại học khối A (Toán – Vật lý – Tiếng Anh), đồng thời xây nền tảng vững chắc từ lớp 6 tại Quận Bình Thạnh (Thầy Lê Văn Thông).

Website tĩnh (Phase 1): HTML5 + [Tailwind CSS (CDN)](https://tailwindcss.com) + Vanilla JavaScript. Không cần build tool.

## Cấu trúc thư mục

```
index.html              trang chủ
programs/                trang chi tiết từng môn học (Lớp 6–12)
  toan.html, vatly.html, anhvan.html
about.html               giới thiệu Thầy Lê Văn Thông
method.html              phương pháp học
schedule.html            lịch khai giảng
assessment.html          form đăng ký tư vấn miễn phí (lead chính, không có bài kiểm tra đầu vào)
results.html             kết quả học viên
public-info.html         thông tin công khai
contact.html             liên hệ + bản đồ
css/styles.css           style bổ sung ngoài Tailwind
js/main.js               menu mobile, accordion FAQ
assets/images/           ảnh thật lấy từ Google Business Profile của trung tâm:
  teacher-whiteboard.jpg   Thầy Lê Văn Thông giảng bài
  classroom-group.jpg      lớp học nhóm
  student-english-study.jpg học viên học Anh văn (dùng trong programs/anhvan.html)
```

## Chạy thử cục bộ

```bash
cd "project-levanthong"  # thư mục này
python3 -m http.server 8000
# mở http://localhost:8000
```

## Nội dung đã cập nhật

- Số điện thoại thật: `0919 222 595`.
- Học phí: `1.500.000đ/tháng` (1 buổi/tuần); học 2-3 buổi/tuần là mức giá thương lượng (liên hệ trung tâm), lớp tối đa `6` học viên, lịch học `1-3 buổi/tuần` tùy nhu cầu, khai giảng đầu mỗi tháng — áp dụng ở `schedule.html` và cả 3 trang `programs/*.html`.
- **Đã bỏ yêu cầu kiểm tra đầu vào**: xóa card "Yêu cầu đầu vào", đổi FAQ liên quan, đổi mọi CTA "Đăng ký kiểm tra đầu vào" thành "Đăng ký tư vấn miễn phí" (`assessment.html` vẫn là trang lead-form chính nhưng không còn framing bắt buộc làm bài test).
- Định hướng thương hiệu: nhấn mạnh "luyện thi đại học khối A" trong khi vẫn giữ phạm vi lớp 6–12 — hero, tagline (`index.html`, footer) đã đổi thứ tự để khối A lên trước.
- Testimonial trên trang chủ, `about.html`, `results.html`: nội dung do Claude soạn theo tinh thần "đồng hành cùng học viên vươn tới mục tiêu đại học" mà anh/chị yêu cầu — **đây là bản nháp**, cần anh/chị duyệt lại hoặc thay bằng cảm nhận thật của học viên/phụ huynh trước khi công bố chính thức.
- Địa chỉ dùng "Phường Bình Lợi Trung" (tên mới sau sáp nhập, đã xác nhận đúng theo anh/chị).

## Còn là placeholder `[ ... ]`

- Video giới thiệu Thầy (chưa có nguồn — trang Facebook trung tâm chưa truy cập được).
- Ảnh bìa sách/tài liệu của Thầy (`about.html`).
- Giấy phép hoạt động, người đại diện pháp lý (`public-info.html`).
- Số liệu thống kê học viên (`results.html`: %, số lượng, số năm hoạt động).
- Google Maps embed thật tại `contact.html` và `index.html` (cần Google Maps Embed API key).

## Tích hợp còn thiếu (Bước 4 của guide)

Form ở `assessment.html` hiện chỉ là HTML tĩnh, **chưa** gửi dữ liệu đi đâu. Cần bổ sung khi có tài khoản/API key:

1. **Google Sheets qua Apps Script** — endpoint nhận dữ liệu form.
2. **reCAPTCHA v3** — chống spam.
3. **Zalo OA** — thông báo lead mới (tùy chọn).
4. **Google Analytics 4** — tracking `page_view`, `view_program`, `start_form`, `submit_form`, `click_phone`, `click_zalo`.
5. **Facebook Pixel** — `PageView`, `ViewContent`, `InitiateCheckout`, `Purchase`.
6. **Google Maps Embed API**.

Xem chi tiết hướng dẫn tích hợp trong `guide-claude-code-website.md`.

## SEO (Bước 6)

Chưa tạo `sitemap.xml`, `robots.txt`, và schema.org JSON-LD. Cần bổ sung trước khi deploy chính thức.
