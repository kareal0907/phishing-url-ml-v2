# Phishing URL Machine Learning Demo V2

Ứng dụng web local dùng Flask để thực nghiệm và so sánh các mô hình Machine Learning trên dữ liệu phishing URL.

**V2 bổ sung:** Trang phân tích URL sâu với tra cứu DNS, WHOIS, SSL/TLS, Blacklist (DNSBL).

## 1. Cài đặt

Yêu cầu: **Python 3.11**

Trong CMD, tại thư mục project:

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Chạy chương trình

```
python app.py
```

Truy cập: http://127.0.0.1:5001

## 3. Các tính năng

### 3.1 Thực nghiệm ML (có sẵn từ V1)
- Upload dataset (CSV/TSV/TXT/JSON/Excel/ARFF/Parquet)
- Train & so sánh 5 model: Logistic Regression, Decision Tree, SVM, Random Forest, XGBoost
- Kết quả: Accuracy, Precision, Recall, F1-score, ROC-AUC, Confusion Matrix, Feature Importance
- Kiểm tra URL nhanh (dùng đặc trưng lexical)

### 3.2 Phân tích URL sâu (MỚI - V2)
Truy cập: **Phân tích URL sâu** trên trang chủ hoặc `/analyze_url`

Tính năng:
- **WHOIS**: Tuổi domain, ngày hết hạn, nhà đăng ký, tổ chức, quốc gia, Name Servers, DNSSEC
- **DNS**: Bản ghi A, MX, NS, TXT
- **SSL/TLS**: Kiểm tra chứng chỉ, nhà cấp, ngày hết hạn
- **Blacklist (DNSBL)**: Kiểm tra IP trong Spamhaus, Barracuda, SpamCop
- **Điểm rủi ro**: 0-100 dựa trên các yếu tố host-based
- **Kết hợp ML**: Nếu đã train model, hiển thị cả dự đoán ML

### Tiêu chí chấm điểm rủi ro
| Yếu tố | Điểm |
|---|---|
| Domain mới tạo (< 30 ngày) | +30 |
| Domain tương đối mới (< 180 ngày) | +15 |
| Không tra được WHOIS | +10 |
| Không có bản ghi DNS A | +20 |
| Không có bản ghi MX | +5 |
| Không có SSL hợp lệ | +15 |
| Không dùng HTTPS | +10 |
| SSL sắp hết hạn (< 15 ngày) | +5 |
| TLD đáng ngờ (.tk, .xyz, .top...) | +15 |
| IP nằm trong blacklist | +25 |
| Domain sắp hết hạn (< 30 ngày) | +10 |

## 4. Dataset có sẵn (thư mục upload/)
- PhiUSIIL_Phishing_URL_Dataset.csv
- PhishingData.arff / PhishingData (2).arff
- dataset_B_05_2020.csv
- train.txt / test.txt / val.txt
