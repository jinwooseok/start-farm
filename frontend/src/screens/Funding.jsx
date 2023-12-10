import React, { useState, useEffect } from "react";
import { FaLeaf } from "react-icons/fa6";
import fetcher from "../fetcher.js";

export default function Funding() {
    const [data, setData] = useState([]);

    const getMessages = async () => {
        const fetchedData = await fetcher("get", "/funding/list/");
        setData(fetchedData);

    };
      
    useEffect(() => {
        getMessages();
        console.log('서버 연결 완료');

    }, []);


    return (
      <main>
        <div className="sub_title">
            <div className="inner_wrap">
                <p>진행중인 <FaLeaf color="#79A73F"></FaLeaf> </p>
                <p>농산물 펀딩을</p>
                <p>확인해보세요</p>
                <span>
                원하는 농작물에 투자하고 재배 후에 신선하고 저렴하게 <br />
                농작물을 받을 수 있어요!
                </span>
            </div>
            <div className="gradient_box"></div>

        </div>
        <div className="funding_list">
            <div className="inner_wrap">


                {data.map((item, index) => ( 
                    <div className="funding_con">
                        <div className="funding_img">
                            <a href={"/Fd_Detail?num="+index}><img src={item.image} alt="" /></a>
                        </div>
                        <span>{item.category}/{item.category_details}</span>
                        <a href={"/Fd_Detail?num="+index}>{item.description} </a>

                        <div className="flex">
                            <span>{item.funding_rate}% 달성</span>
                            <p>{item.price}원</p>
                        </div>
                    </div>
                ))}

            </div>
        </div>
      </main>
    );
  }