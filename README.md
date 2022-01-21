# 목적
장고를 사용해서 애플리케이션을 만들고 서버까지 구성해본다. 백엔드에서 어떤 처리를 하는지와 DB에 대해 이해하고 ORM을 다루는 방법을 익힌다.

### **구현 내용**

#### **Model 정의**

![django-board](https://user-images.githubusercontent.com/94369511/148603972-e46dac30-75a1-4f06-b5f4-12cbb9e3c982.png)

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

![image](https://user-images.githubusercontent.com/94369511/148216842-3a4f0ef7-c122-4380-bc13-682de65ba73b.png)

![image](https://user-images.githubusercontent.com/94369511/148216889-8b49f50f-3ef3-4bb7-826e-f562df8e8aaf.png)

-   추가한 내용
    -   댓글 알림
    -   유저가 작성한 글/댓글 보기
    -   게시글 수, 댓글 수
    -   게시글에 이미지 삽입



2022.01.08
-   수정한 내용
    -   화면 크기에 따른 이미지 사이즈
    -   댓글 입력 중 엔터키 입력시 댓글 등록, Shift+엔터키 입력시 줄바꿈

2022.01.10
-   추가한 내용
    -   게시판 추가
    -   24시간 이내 글에 강조표시
    -   메인 페이지 생성

2022.01.21
-   수정한 내용
    -   N+1 쿼리 수정 ( post_detail.html 에서 댓글 가져오기, 댓글 작성 시 해당 게시글에 작성한 댓글의 유저 목록 가져오기 )
