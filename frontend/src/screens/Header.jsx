import '../App.css';




export default function Header() {

  
  return (
    <header>
      <div>
        <h3 className='logo'><a href="/">스타트 팜</a></h3>
        <ul className="menu">
          <li><a href="/Farm">귀농 한달살이</a></li>
          <li><a href="/Funding">농산물 펀딩</a></li>
          <li><a href="/Clean">클린 농촌마을</a></li>
        </ul>
      </div>
      <p>귀농의 처음부터 끝까지!</p>
    </header>
  );
}
