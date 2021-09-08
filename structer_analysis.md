# Yes24 blog 구조 분석
* 리뷰만 모아진 페이지 : http://blog.yes24.com/BlogMain/Review/Review
* 새로운 리뷰만 모아진 페이지 : http://blog.yes24.com/BlogMain/Review/NewReview
* 카테고리로 접근 : http://blog.yes24.com/BlogMain/Review/NewReview?c1=001
    - c1=숫자 로 카테고리 지정해서 검색
* 페이지 인덱스 추가 : http://blog.yes24.com/BlogMain/Review/NewReview?c1=001&PageNumber=2
    - &PageNumber=숫자 를 넣는다.

## 카테고리
* c1 = 001 : 국내도서
* c1 = 002 : 외국도서
* c1 = 003 : CD/LP
* c1 = 004 : DVD/Blu-ray
* c1 = 006 : 문구/GIFT
* c1 = 017 : ebook
* c1 = tkt : 공연

1. 매일 새벽 12시에 그날 올라온 리뷰들을 크롤링
2. NewReview에 있는 목록 중 그 전달 하루치 모두 크롤링한다. ex) 9월 10일 자정엔 9월 9일 게시글을 모두 크롤링
    - 날짜의 위치
    ```html
    <div class="gul rvgul">
        <ul>
            <li>
                <a href="url">
                <p class="gulinfo">
                    <a href="url">
                    " | "
                    <span nickname>
                    " | 날짜"
                </p>
            </li>
        </ul>
    </div>
    ```
3. url로 접속해서 리뷰를 크롤링한다.
    - content의 위치
    ```html
    <div class="blogContArea">
        <span id="cphMain_dlArtList_lbArtCont_0">
        </span>
    </div>
    ```
    - 주의할 점 : 글씨체를 설정하는 태그가 있다. 이런 것들은 제거해줘야 한다.

4. 책에 대한 정보도 없으면 같이 저장한다.
    - url의 위치
    ```html
    <div id="cphMain_dlArtList_dvReviewGoods_0">
    ...
        <p id="cphMain_dlArtList_ReviewGoodsTitle_0">
            <a href="url" target="view_goods">
        </p>
    </div>
    ```
    - url속 상품코드 찾기 : /lib/adon/View.aspx?blogid=342939&goodsno=103304588&adon_type=R&regs=b&art_bl=15031109
    - 위에서 보면 goodsno= 하고 나오는 것이 상품 정보이다.
