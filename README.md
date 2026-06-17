# 클래식 기타 연주자 포트폴리오 웹사이트

HTML5, CSS3, 순수 JavaScript, Bootstrap 5를 사용하여 만든 모던하고 세련된 개인 포트폴리오 웹사이트입니다.

## 기능

- **개인 프로필**: 클래식 기타 연주자 소개
- **음악 & 악보 관리**: 음악 파일과 악보를 추가하고 삭제할 수 있는 기능 (LocalStorage 사용)
- **연락처 폼**: 이름, 연락처, 이메일, 메시지를 입력하여 전송 (Formspree 사용)
- **반응형 디자인**: 모바일, 태블릿, 데스크톱 모두 지원
- **모던한 UI**: 그라데이션, 애니메이션, 부드러운 전환 효과

## 사용된 기술

- HTML5
- CSS3 (Custom CSS + Bootstrap 5)
- 순수 JavaScript (Vanilla JS)
- Bootstrap 5.3.2
- Bootstrap Icons
- Formspree (이메일 전송)

## Netlify 배포 방법

### 1. Formspree 계정 설정

1. [Formspree](https://formspree.io/)에 무료 계정을 생성합니다.
2. 새 폼을 생성하여 Form ID를 받습니다.
3. `index.html` 파일의 127번 라인에서 `YOUR_FORM_ID`를 실제 Form ID로 변경합니다:
   ```html
   <form id="contactForm" action="https://formspree.io/f/YOUR_ACTUAL_FORM_ID" method="POST">
   ```

### 2. Netlify에 배포

#### 방법 A: Git을 통한 배포 (권장)

1. GitHub, GitLab, 또는 Bitbucket에 이 프로젝트를 푸시합니다.
2. [Netlify](https://www.netlify.com/)에 로그인합니다.
3. "New site from Git"을 클릭합니다.
4. 저장소를 선택하고 배포 설정을 완료합니다.

#### 방법 B: Netlify Drop 사용

1. [Netlify Drop](https://app.netlify.com/drop)에 접속합니다.
2. `myai` 폴더를 드래그 앤 드롭합니다.
3. 자동으로 배포가 완료됩니다.

### 3. 배포 후 설정

1. Netlify 대시보드에서 사이트 설정을 엽니다.
2. Domain settings에서 원하는 도메인을 설정합니다.
3. Formspree에서 이메일 수신 설정을 확인합니다.

## 파일 구조

```
myai/
├── index.html      # 메인 HTML 파일
├── styles.css      # 스타일시트
├── script.js       # JavaScript 기능
├── netlify.toml    # Netlify 설정 파일
└── README.md       # 이 파일
```

## 사용자 정의

### 연락처 정보 변경

`index.html` 파일의 연락처 섹션에서 다음 정보를 수정하세요:
- 전화번호 (119번 라인)
- 이메일 (127번 라인)
- 위치 (135번 라인)

### 프로필 정보 변경

`index.html` 파일의 프로필 섹션에서 다음 정보를 수정하세요:
- 이름 및 소개 (73-80번 라인)
- 전문 분야 (82-88번 라인)

### 색상 테마 변경

`styles.css` 파일의 `:root` 섹션에서 색상 변수를 수정하세요:
```css
:root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    --accent-color: #e74c3c;
    /* ... */
}
```

## 음악/악보 관리

- 웹사이트에서 직접 음악이나 악보를 추가할 수 있습니다.
- 데이터는 브라우저의 LocalStorage에 저장됩니다.
- 삭제 버튼을 클릭하여 항목을 삭제할 수 있습니다.

## 브라우저 호환성

- Chrome (최신 버전)
- Firefox (최신 버전)
- Safari (최신 버전)
- Edge (최신 버전)

## 라이선스

이 프로젝트는 개인 포트폴리오 용도로 자유롭게 사용 및 수정할 수 있습니다.
