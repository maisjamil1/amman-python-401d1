import styles from '../static/css/styles.module.css'
import Header from '../components/Header'
import Footer from '../components/Footer'

export default function Home(props){
  return (
    <div className={styles.hello}>
        <Header />
        <h2>{props.users[0].first_name} {props.users[0].last_name}</h2>
        <img src={props.users[0].avatar} />
        <Footer users={props.users}/>
    </div>
  )
}

export async function getServerSideProps(){
    // Call api here
    // Add data to props
    const res = await fetch('https://reqres.in/api/users');
    const dataObj = await res.json();
    console.log(dataObj);
    return { props: {users: dataObj.data} };
}
