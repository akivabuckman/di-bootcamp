const data = require("../data.json");

const PostList = (props) => {
    return(
        <>
        <h1>Hi this is a title</h1>
        {data.map(i => {
            return (
                <div>
                    <h1>{i.title}</h1>
                    <p>{i.content}</p>

                </div>
                )
            })
        }
        </>  
    )
}
export default PostList