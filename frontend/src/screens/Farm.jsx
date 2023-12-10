import { FaLeaf, FaBuildingWheat, FaBus, FaChildDress, FaChild, FaChildren, FaCircleCheck} from "react-icons/fa6";
import React, { useState, useEffect } from "react";
import fetcher from "../fetcher.js";

export default function Farm() {
    const [data, setData] = useState([]);
    const [con, setCon] = useState();
    const [title, setTitle] = useState();
    const [num, setNum] = useState(0);
    const [img, setImg] = useState();

    const getMessages = async () => {
        const fetchedData = await fetcher("get", "/farm/program/list/");
        setData(fetchedData);
        setTitle(fetchedData[0].title);
        setCon(fetchedData[0].description);
        setImg(fetchedData[0].image);
    };
      
    useEffect(() => {
        getMessages();
        console.log('서버 연결 완료');

    }, []);

    function btn(index){
        setNum(index);
        setTitle(data[index].title);
        setCon(data[index].description);
        setImg(data[index].image);

    }


    return (
      <main>
        <div className="sub_title center">
            <div className="inner_wrap">
                <p>호남지역 최초 최대 제휴 <FaLeaf color="#79A73F"></FaLeaf> </p>
                <p>스타트 팜의 한달살기 프로그램을</p>
                <p>직접 경험해보세요!</p>
                <ul className="card">
                   <li><FaBuildingWheat size={120}></FaBuildingWheat><span>제휴농가</span><h3>1,500+</h3></li>
                   <li><FaChildDress size={120}></FaChildDress><span>프로그램 참여자 수</span><h3>2,500+</h3></li>
                   <li><FaBus size={120}></FaBus><span>한달살이 후 귀농인</span><h3>320+</h3></li>
                </ul>
            </div>
            <div className="gradient_box"></div>
        </div>

        <div className="Farm">
            <div className="con_title">농촌 한달살이</div>
            <p>“체험자 모집부터 농가 매칭까지”<br />스타트팜의 다양한 농가를 확인해보세요.</p>
            <div className="inner_wrap">
                <div className="Farm_list">
                    <p>한달살기 프로그램</p>
                    <span>스타트 팜이 검증한 농가들과 함께 농업 노하우를 배우세요!</span>
                    {data.map((item, index) => (
                    <div className={`Farm_con ${num === index ? "chk" : ""}`} onClick={() => btn(index)}>
                         <div className="icon"><FaChild size={22} color="#fff"></FaChild></div>
                         <div className="Farm_text"><h3>{item.title}</h3><p>{item.town}</p></div>
                         <FaCircleCheck size={45} className="circle-check"  ></FaCircleCheck>
                     </div>
                    ))}
                </div>
                <div className="Farm_box">
                    <h3><div className="icon"><FaChild size={22} color="#fff"></FaChild></div> {title} </h3>
                    <p>{title}</p>
                    <span>{con}</span>
                    <div className="Farm_img">
                        <img src={img} alt="" />
                    </div>
                    <a href={"/Ask?num="+num} className="Farm_btn">
                        한달살이 신청하러 가기
                    </a>
                </div>
            </div>
        </div>
       
            
      </main>
    );
  }