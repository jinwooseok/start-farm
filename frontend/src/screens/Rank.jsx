import { FaLeaf } from "react-icons/fa6";
import React, { useState, useEffect } from "react";
import fetcher from "../fetcher.js";




export default function Rank() {
    
    const [msg, setMsgs] = useState([]);

    const getMessages = async () => {
        const msgs = await fetcher("get", "/town/ranking");
        setMsgs(msgs);
      };
      
    useEffect(() => {

      getMessages();
      console.log('서버 연결 완료');
      console.log(msg);
    }, []);


    
    return (

        <div className="rank_boxs">
            <div className="rank_box">
                <div className="rank_box_top">
                    <h3>지역, 지역, 지역</h3>
                    <a href="#">더보기</a>
                </div>
                <ul className="rank_lists">
                    <li>
                        <p>1위</p>
                        <div className="rank_img"><a href="#"></a></div>
                        <span><a href="#">OO마을</a></span>
                        <h3>9.2<em>/10</em></h3>
                    </li>
                    <li>
                        <p>2위</p>
                        <div className="rank_img"><a href="#"></a></div>
                        <span><a href="#">OO마을</a></span>
                        <h3>9.2<em>/10</em></h3>
                    </li>
                    <li>
                        <p>3위</p>
                        <div className="rank_img"><a href="#"></a></div>
                        <span><a href="#">OO마을</a></span>
                        <h3>9.2<em>/10</em></h3>
                    </li>
                    <li>
                        <p>4위</p>
                        <div className="rank_img"><a href="#"></a></div>
                        <span><a href="#">OO마을</a></span>
                        <h3>9.2<em>/10</em></h3>
                    </li>
                    <li>
                        <p>5위</p>
                        <div className="rank_img"><a href="#"></a></div>
                        <span><a href="#">OO마을</a></span>
                        <h3>9.2<em>/10</em></h3>
                    </li>
                </ul>
            </div>
        
        </div>
            
    );
  }