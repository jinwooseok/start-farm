import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
export default function Ask() {

    const MyBackButton = () => {
        const navigate = useNavigate();
        const onClickBtn = () => {
          navigate(-1);
        };
        return (
          <button className="back" onClick={onClickBtn}>취소</button>
        );
      };

    const [name, setName] = useState(""); 
    const [age, setAge] = useState(""); 
    const [number, setNumber] = useState(""); 
    const [email, setEmail] = useState(""); 
    const [ask, setAsk] = useState(""); 

    const handleNameChange = (event) => {
        setName(event.target.value);
    };
    const handleAgeChange = (event) => {
        setAge(event.target.value);
    };
    const handleNumberChange = (event) => {
        setNumber(event.target.value);
    };
    const handleEmailChange = (event) => {
        setEmail(event.target.value);
    };
    const handleAskChange = (event) => {
        setAsk(event.target.value);
    };

  return (
    <main>
        <div className="inner_wrap">
        <div className="board-list">
        <div className="section-title">
          <h2>한달살이 신청</h2>
          <p className="notice-text">
            궁금하신 내용을 자세히 남겨주시면 보다 정확한 답변을 이메일로 전달해드리겠습니다.
          </p>
        </div>
        <form action="" method="post">
            <div className="inputs">
                <div className="radios">
                    <ul class="data-list">
                        <p className="require">신청 이유</p>
                        <input id="ASK_USER_DIV" name="ASK_USER_DIV" required="required" type="hidden" value="" />
                        <li className="radio"><input type="radio" id="show1_1" name="CHK_ASK" value="1" checked /><label for="show1_1">귀농 전 체험</label></li>
                        <li className="radio"><input type="radio" id="show1_2" name="CHK_ASK" value="2" /><label for="show1_2">힐링 한달살이</label></li>
                        <li className="radio"><input type="radio" id="show1_3" name="CHK_ASK" value="3" /><label for="show1_3">농업 기술 습득</label></li>
                        <li className="radio"><input type="radio" id="show1_4" name="CHK_ASK" value="ETC" /><label for="show1_4">기타</label></li>
                    </ul>
                </div>
            </div>
            <div className="inputs">
                <div className="input-box">
                    <p className="require">이름</p>
                    <input id="name" name="name" required type="text" value={name} onChange={handleNameChange}></input>
                </div>
                <div className="input-box">
                    <p className="require">나이</p>
                    <input id="age" name="age" required type="text" value={age} onChange={handleAgeChange}></input>
                </div>
            </div>
            <div className="inputs">
                <div className="input-box">
                    <p className="require">연락처</p>
                    <input id="number" name="number" required type="text" value={number} onChange={handleNumberChange}></input>
                </div>
                <div className="input-box">
                    <p className="require">이메일</p>
                    <input id="email" name="email" required type="email" value={email} onChange={handleEmailChange}></input>
                </div>
            </div>
            <div className="ask">
                <p>질문 사항 & 건의 사항</p>
                <textarea name="ask" id="ask" value={ask} onChange={handleAskChange}></textarea>
            </div>
            <div className="btn-area">
                <MyBackButton></MyBackButton>
                <button className="submit" type="submit">신청하기</button>
            </div>
        </form>
      </div>
        </div>
    </main>
  );
}