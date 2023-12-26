
import React, { useState } from "react";
import { FaChevronDown } from "react-icons/fa6";
import { ScrollTrigger } from "react-scroll-trigger";
import gsap from "gsap"; // gsap 라이브러리 임포트
import { GiFarmer } from "react-icons/gi" ;
import { FaUsers } from "react-icons/fa";
import { BiUser } from "react-icons/bi";



export default function Main() {
  const [num, setNum] = useState(1);

  const bannerRef = React.useRef(null);

  function numbtn (number){
    setNum(number);
  }

  // 컴포넌트가 마운트된 후 애니메이션 실행
  React.useEffect(() => {
    // gsap 애니메이션 코드
    const bannerElement = bannerRef.current;

    gsap.fromTo(
      bannerElement,
      { opacity: 0, y: -20 },
      { opacity: 1, y: 0, duration: 1, ease: "power2.out" }
    );
  }, []);
    return (
      <main>
        <div className="banner" >
          <div className="inner_wrap">
            <p ref={bannerRef}>귀농의 처음부터 끝까지</p>
            <h3>귀농/귀촌 통합 플랫폼</h3>
            <h2>START FARM</h2>
          </div>
        </div>
        <div className="main_menu">
          <div className={`menu_box ${num === 1 ? "on" : ""}`} onClick={() => numbtn(1)}>
              <div className="menu_text">
                <p>농업인</p>
                <h3>농사 지으시는데</h3>
                <h3>일손 부족하진 않으세요?</h3>
                <a href="/Farmer">농업인 신청</a>
              </div>
              <div className="go_btn1">
                <button onClick={() => numbtn(1)}>
                  <FaChevronDown size="33"></FaChevronDown>
                </button>
              </div>
          </div>
          <div className={`menu_box ${num === 2 ? "on" : ""}`} onClick={() => numbtn(2)}>
              <div className="go_btn2">
                <button onClick={() => numbtn(2)}>
                  <FaChevronDown size="33"></FaChevronDown>
                </button>
              </div>
              <div className="menu_text">
                <p>농업인</p>
                <h3>나에게 꼭 맞는</h3>
                <h3>농촌 한달살이 지원하세요</h3>
                <a href="/Farm">농촌 한달살이 보기</a>

              </div>

          </div>
        </div>
        <div className="main_con1">
          <div className="con_title">농촌 한달살이</div>
          <h3 className="con_text">귀농 희망자, 한달간 농업기술을 배우며</h3>
          <h3 className="con_text">일해보는건 어떤가요?</h3>
          <p className="con_text_sub">스타트팜에서 확인된 농업인만!</p>
          <a href="/Farm" className="con_btn">농촌 한달살이 보러가기</a>
          <div className="visual_boxs">
            <div className="visual_imgs">
              <div className="visual_box">
                <div className="visual_img">

                  <FaUsers size={200}></FaUsers>
                </div>
                <div>
                  <p>BEGINNER</p>
                  <h3>귀농 희망자</h3>
                </div>
              </div>
              <div className="arrows">
                <img src={'./image/Arrow.png'} alt="img" />
                <img src={'./image/Arrow.png'} alt="img" />
                <img src={'./image/Arrow.png'} alt="img" />
              </div>
              <div className="visual_box">
                <div className="visual_img">
                  <p className="visual_title">스타트 팜</p>
                </div>
                <div>
                <h2 className="">한달살이 신청</h2>
              </div>
              </div>
              <div className="arrows">
                <img src={'./image/Arrow.png'} alt="img" />
                <img src={'./image/Arrow.png'} alt="img" />
                <img src={'./image/Arrow.png'} alt="img" />
              </div>
              <div className="visual_box">
                <div className="visual_img">
                <img src={'./image/farmer.png'}  alt="" />
                </div>
                <div>
                  <p>FARMER</p>
                  <h3>농업인</h3>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="main_con2">
          <div className="con_title" >농산물 펀딩</div>
          <h3 className="con_text">농산물 판매,</h3>
          <h3 className="con_text">직거래 펀딩으로 마케팅 예산을 절감하세요.</h3>
          <p className="con_text_sub">최대 65% 절감 효과!</p>
          <a href="/Funding" className="con_btn">농산물 펀딩 보러가기</a>
          <div className="visual_boxs">
            <div className="visual_imgs">
              <div className="visual_box">
                <div className="visual_img">
                  <FaUsers size={200}></FaUsers>
                </div>
              <div>
                <p>BUYER</p>
                <h3>농산물 구매자</h3>
              </div>
              </div>
              <div className="arrows">
                <img src={'./image/Arrow.png'} alt="img" />
                <img src={'./image/Arrow.png'} alt="img" />
                <img src={'./image/Arrow.png'} alt="img" />
              </div>
              <div className="visual_box">
                <div className="visual_img">
                  <p className="visual_title">스타트 팜</p>
                </div>
                <div>
                <h2 className="">예약구매 신청</h2>

              </div>
              </div>
              <div className="arrows">
                <img src={'./image/Arrow.png'} alt="img" />
                <img src={'./image/Arrow.png'} alt="img" />
                <img src={'./image/Arrow.png'} alt="img" />
              </div>
              <div className="visual_box">
                <div className="visual_img">
                <img src={'./image/farmer.png'}  alt="" />
                </div>
                <div>
                <p>FARMER</p>
                <h3>농업인</h3>
              </div>

              </div>
            </div>


          </div>
        </div>
        <div className="main_con3">
          <div className="inner_wrap">
          <div className="con_box">
            <h3>클린 농촌마을,</h3>
            <h3>호남 지역의 살기 좋은</h3>
            <h3>클린마을를 확인해보세요</h3>
            <a href="/Clean">클린 농촌 마을순위보기</a>
          </div>
          <img src={'./image/map.png'} alt="" />
          </div>
        </div>
      </main>
    );
  }