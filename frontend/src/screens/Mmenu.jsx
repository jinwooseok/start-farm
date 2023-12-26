import '../App.css';
import { AiOutlineClose } from "react-icons/ai";



export default function Mmenu() {

    function menuCtrl(){
        const menu = document.getElementById("m-menu");
        console.log(menu.style.right);
        if(menu.style.right == "0px"){
            menu.style.right = "-100%";
        }else {
            menu.style.right = "0";
        }
    }
  
  return (
    <div id="m-menu" className='mb'>
        <AiOutlineClose className='closebtn' onClick={menuCtrl}/>
        <ul className="menus">
          <li><a href="/Farm">귀농 한달살이</a></li>
          <li><a href="/Funding">농산물 펀딩</a></li>
          <li><a href="/Clean">클린 농촌마을</a></li>
        </ul>
    </div>
  );
}
