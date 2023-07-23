const LanguageMaker = (props) => {
    const i = props.language;
    const handleClick = props.handleClick;

    return <>
          <div className="languageBox">
            <div className="countBox">
              <p>
                {i.votes}
              </p>
            </div>
            <div className="nameBox">
              <p>
                {i.name}
              </p>
            </div>
            <div className="buttonBox">
                <button onClick={() => handleClick(i)}>Click Here</button>
            </div>
          </div>
        </>
}

export default LanguageMaker