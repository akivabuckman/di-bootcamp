import React from "react";

class ErrorBoundary extends React.Component {
    constructor(props) {
        super(props);
        this.state = {hasError: false};
    }
    componentDidCatch(error, errorInfo) {
        this.setState({hasError: true})
    }

    render(){
        if (this.state.hasError) {
            return <div>Something went wrong</div>
        }
        return this.props.children
    }
}

export default ErrorBoundary