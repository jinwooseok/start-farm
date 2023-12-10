import { useNavigate,useLocation } from 'react-router-dom';
import React, { useState, useEffect } from "react";
import fetcher from "../fetcher.js";

export default function Fd_Detail() {
    const location = useLocation();
    const searchParams = new URLSearchParams(location.search);
    const num = searchParams.get('num');

    const navigate = useNavigate();
 
    const fd = () => {
      alert("펀딩이 되었습니다.");
      navigate("/");
    };



    const [data, setData] = useState([]);

    const getMessages = async () => {
        const fetchedData = await fetcher("get", "/funding/list/");
        setData(fetchedData[num]);

    };
      
    useEffect(() => {
        getMessages();
        console.log('서버 연결 완료');

    }, []);


    return (
        <main>
            <div className="inner_wrap">
                <div className="Fd">
                    <div className="Fd_img">
                        <img src={data.image} alt="" />
                    </div>
                    <div className="Fd_box">
                        <span>{data.area}</span>
                        <h3>{data.description}</h3>
                        <h5>{data.price}원</h5>
                        <p>해당 상품은 {data.funding_rate}%의 펀딩을 달성했어요.</p>
                        <div className="Fd_text">
                            <span>제품 설명</span>
                            <div>
                                <p>{data.name}</p>
                                <span>{data.detail_description}</span>
                            </div>
                        </div>
                        <div className="Fd_text">
                            <span>판매자</span>
                            <div>
                                <p>{data.user}</p>
                            </div>
                        </div>
                        <div className="Fd_text">
                            <span>펀딩 예상기간</span>
                            <div>
                                <p>{data.period}개월</p>
                            </div>
                        </div>
                        <div className="Fd_text">
                            <span>포장방법</span>
                            <div>
                                <p>스티로폼 박스</p>
                            </div>
                        </div>
                        <div className="Fd_text">
                            <span>판매단위</span>
                            <div>
                                <p>{data.unit}</p>
                            </div>
                        </div>
                        <div className="Fd_text">
                            <span>안내사항</span>
                            <div>
                                <p>배송일자에는 작은 변동이 있을 수 있습니다.</p>
                            </div>
                        </div>
                        <button onClick={fd} className="Fd_btn">
                            펀딩 하기
                        </button>
                    </div>
                </div>
            </div>
        </main>
    );
  }