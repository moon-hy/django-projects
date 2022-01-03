## **상황**
튜토리얼을 따라서 간단한 구현 자체는 어느정도 완료한듯 싶다. html과 css를 잘 다루지 못해서 그래도 조금 그럴싸하게 꾸미는데에 시간을 훨씬 많이 잡아먹은것 같다. 이런 부분은 앞으로 좀 더 중요도를 생각해서 진행하도록 해야겠다.

### **구현 내용**

#### **Model 정의**
[##_Image|kage@bfLnLD/btrpHFqlsJT/5KL49I7IK8JJrwNL8D3nm0/img.png|CDM|1.3|{"originWidth":821,"originHeight":573,"style":"alignCenter"}_##]

#### **메인 화면**
[##_Image|kage@bLLmYq/btrpus696Ci/Qr64I0phu4ewhsR3mEMkwk/img.png|CDM|1.3|{"originWidth":1233,"originHeight":481,"style":"alignCenter"}_##]
-   상단 바
    -   메인 화면으로 이동, 로그인/로그아웃, 메뉴 버튼
    -   메뉴 버튼: 오프캔버스 메뉴, 메뉴 리스트는 언제든지 쉽게 변경할 수 있도록 html 분리
-   게시판
    -   Recent/Hits/Like/Reply Select Box: 개수별 게시글 정렬
    -   글쓰기 버튼: 게시글 생성 페이지
    -   게시글 번호, 제목 \[댓글 수\], 작성자, 작성 일시, 조회수, 추천 수 표시
    -   페이지네이션: 한 페이지에 최대 n개의 게시글만 표시하고 페이지를 나눔
      -   첫 페이지, 이전 페이지, 페이지 번호 선택, 다음 페이지, 끝 페이지로 이동 기능
    -   검색: 게시글, 내용, 작성자, 댓글에서 검색

#### **게시글**
[##_Image|kage@by8OYu/btrpzJUXDJR/kpFnDf01H6i3BGbHfWZN6k/img.png|CDM|1.3|{"originWidth":1007,"originHeight":872,"style":"alignCenter"}_##]

-   게시글
    -   제목, 작성 일시, 작성자, 수정/삭제 버튼
    -   게시글 내용
    -   추천/비추천 수 및 버튼
    -   댓글: 작성자, 내용, 작성 일시, 삭제 버튼
    -   댓글 다는 영역
-   생각나는 추가해야 할 사항
    -   댓글 알림
    -   대댓글
    -   특정 유저가 작성한 글/댓글 보기
    -   내 게시글 수, 댓글 수
    -   소셜 로그인 (OAuth)
    -   회원 탈퇴
    -   게시글에 이미지
      -   썸네일
