export default function UserDetails(props){
    return (
        <>
            <h1>{props.user.first_name} {props.user.last_name}</h1>
            <img src={props.user.avatar}></img>
        </>
    )
}

export async function getServerSideProps(context){
    const id = context.query.id
    const res = await fetch(`https://reqres.in/api/users/${id}`);
    const dataObj = await res.json();
    return { props: {user: dataObj.data} };
}
