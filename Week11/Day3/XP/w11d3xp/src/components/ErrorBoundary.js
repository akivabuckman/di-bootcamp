import React from "react";


class ErrorBoundary extends React.Component {
    constructor(props){
      super(props);
      this.state = {
        error: null,
        hasError: false,
        errorInfo: ""
      }
    }

    // static getDerivedStateFromError(error) {
    //     return {hasError:true}
    // }

    componentDidCatch(error, errorInfo) {
        this.setState({
            error: error,
            errorInfo: errorInfo,
            hasError: true
        })
    }

    render(){
        if (this.state.hasError) {
            return (
                <>
                <details style={{ whiteSpace: 'pre-wrap' }}>
                    {this.state.error && this.state.error.toString()}
                    <br />
                    {this.state.errorInfo.componentStack}
                </details>
                </>
            )
        }
        return this.props.children;

    }
}

export default ErrorBoundary