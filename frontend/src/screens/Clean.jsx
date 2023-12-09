import React, { useState, useEffect } from "react";
import { FaLeaf } from "react-icons/fa6";
import fetcher from "../fetcher.js";

export default function Clean() {
    
    const [data, setData] = useState([]);
    const [time, setTime] = useState();

    const getMessages = async () => {
        const fetchedData = await fetcher("get", "/town/ranking/");
        setData(fetchedData.ranking);
        setTime(fetchedData.update_at);
    };
      
    useEffect(() => {
        getMessages();
        console.log('서버 연결 완료');
        console.log(data);
    }, []);

    return (
        <main>
            <div className="sub_title">
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
            </div>
            <div className="rank">
                <div className="inner_wrap">
                    <div class="rank_head">
                            <p>호남 농촌 클린마을 순위</p>        
                            <span>업데이트 일시 <em>{time}</em></span>
                    </div>
                    <div className="rank_boxs">
                        {Object.entries(data).map(([region, rankingArray], idx) => (
                            <div className="rank_box" key={region}>
                                <div className="rank_box_top">
                                    <h3>{region}</h3>
                                    <a href={"/Clean_more?num="+idx}>더보기</a>
                                </div>
                                <ul className="rank_lists">
                                {rankingArray.slice(0, 5).map(([img, village, score], index) => (
                                    <li key={index}>
                                        <p>{index + 1}위</p>
                                        <div className="rank_img"><a href="#"><img src={"http://localhost:8000" + img} alt="" /></a></div>
                                        <span><a href="#">{village}</a></span>
                                        <h3>{score !== null ? score.toFixed(1) : 'N/A'}<em>/5</em></h3>
                                    </li>
                                ))}
                                </ul>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </main>
    );
}
