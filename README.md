튜토리얼을 따라서 간단한 구현 자체는 어느정도 완료한듯 싶다. html과 css를 잘 다루지 못해서 그래도 조금 그럴싸하게 꾸미는데에 시간을 훨씬 많이 잡아먹은것 같다. 이런 부분은 앞으로 좀 더 중요도를 생각해서 진행하도록 해야겠다.

### **구현 내용**

#### **Model 정의**
![image](https://user-images.githubusercontent.com/94369511/147909455-d868bcbf-39d9-40e3-b42b-c11193e0c5b1.png)

#### **메인 화면**
![image](https://user-images.githubusercontent.com/94369511/147909437-beb12cb6-36e1-4816-8b30-e8a8696040c4.png)
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
![image](https://user-images.githubusercontent.com/94369511/147909449-a5645445-7813-47c0-889f-07143894d440.png)

-   게시글
    -   제목, 작성 일시, 작성자, 수정/삭제 버튼
    -   게시글 내용
    -   추천/비추천 수 및 버튼
    -   댓글: 작성자, 내용, 작성 일시, 삭제 버튼
    -   댓글 다는 영역

2022.01.05
![image](https://user-images.githubusercontent.com/94369511/148181875-2dbdaac2-4b20-49fe-bff9-58609fa29442.png)
![image](https://user-images.githubusercontent.com/94369511/148181938-52f1e00e-3a22-4fc7-b786-40b2a08efcf8.png)
![image](https://user-images.githubusercontent.com/94369511/148182045-555633c1-a5ee-4f9f-aa23-e067e8ae1b48.png)

-   추가한 내용
    -   댓글 알림
    -   유저가 작성한 글/ 댓글 보기
    -   게시륵에 이미지 삽입 가능

-   TO DO
    -   대댓글
    -   소셜 로그인 (OAuth)
    -   회원 탈퇴
    -   썸네일
