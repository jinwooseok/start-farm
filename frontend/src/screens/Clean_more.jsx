import React, { useState, useEffect } from "react";
import { useNavigate,useLocation } from 'react-router-dom';
import { FaLeaf } from "react-icons/fa6";
import fetcher from "../fetcher.js";

export default function Clean() {
    const location = useLocation();
    const searchParams = new URLSearchParams(location.search);
    const num = searchParams.get('num');

    
    const [data, setData] = useState([]);
    const [title, setTitle] = useState([]);
    const [time, setTime] = useState();

    const getMessages = async () => {
        const fetchedData = await fetcher("get", "/town/ranking/");
        const keys = Object.keys(fetchedData.ranking);
        setData(fetchedData.ranking[keys[num]]);
        setTitle(keys[num]);
        setTime(fetchedData.update_at);
        console.log(keys[num]);
    };
      
    useEffect(() => {
        getMessages();
        console.log('서버 연결 완료');
        console.log(data);
    }, []);

    return (
        <main>
            {/* <div className="sub_title">
                <div className="inner_wrap">
                    <p>호남 농촌 <FaLeaf color="#79A73F"></FaLeaf> </p>
                    <p>클린마을 순위를</p>
                    <p>확인해 보세요</p>
                    <span>
                        귀농 희망자들을 위한 마을 별 평가에 기반한 순위입니다. <br />
                        여러 클린마을 랭킹을 알아보세요!
                    </span>
                </div>
                <div className="gradient_box"></div>
            </div> */}
            <div className="rank">
                <div className="inner_wrap">
                    <div class="rank_head">
                        <p>{title} 클린마을 순위</p>        
                        {/* <p>클린마을 순위</p>         */}
                        <span>업데이트 일시 <em>{time}</em></span>
                    </div>
                    <div className="rank_boxs">
                        <div className="rank_box_more">

                            <ul className="rank_lists">
                                {data.map(([img,village, score, area_welfare, town_welfare, town_culture, town_facility,town_citizen], index) => (
                                    <li key={index}>
                                        <p>{index + 1}위</p>
                                        <div className="rank_img"><a href="#"><img src={img} alt="" /></a></div>
                                        <span><a href="#">{village}</a></span>
                                        <h5>지역 복지:<span>{area_welfare}</span> 마을 복지:<span>{town_welfare}</span> 마을 문화:<span>{town_culture}</span> 마을 시설:<span>{town_facility}</span> 마을 주민:<span>{town_citizen}</span></h5>
                                        <h3>{score !== null ? score.toFixed(1) : 'N/A'}<em>/5</em></h3>
                                    </li>
                                ))}
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </main>
    );
}
