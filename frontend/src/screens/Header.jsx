import '../App.css';
import { MdOutlineMenu } from "react-icons/md";



export default function Header() {

  function menuCtrl(){
    const menu = document.getElementById("m-menu");
    if(menu.style.right == 0){
        menu.style.right = "-100%";
    }else {
        menu.style.right = "0";
    }
}
  return (
    <header>
      <div>
        <h3 className='logo'><a href="/">스타트 팜</a></h3>
        <ul className="menu pc">
          <li><a href="/Farm">귀농 한달살이</a></li>
          <li><a href="/Funding">농산물 펀딩</a></li>
          <li><a href="/Clean">클린 농촌마을</a></li>
        </ul>
      </div>
      <p className='pc'>귀농의 처음부터 끝까지!</p>
      <MdOutlineMenu className="mb m-btn" onClick={menuCtrl}/>

    </header>
  );
}
