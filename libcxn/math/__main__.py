import uvicorn
import argparse

def main():
    parser = argparse.ArgumentParser(description="Run the Backwards Compatible WizTLE REST API.")
    parser.add_argument("--port", type=int, default=8000, help="Port number (default: 8000)")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host (default: 0.0.0.0)")
    parser.add_argument("--workers", type=int, default=1, help="Number of worker processes")
    args = parser.parse_args()

    uvicorn.run(
        "wiztle.viscomp:app",
        host=args.host,
        port=args.port,
        workers=args.workers,
        log_level="info",
        # Production flags:
        reload=False,
        loop="uvloop",  # Use high-performance event loop (optional)
        http="httptools",  # Explicitly select httptools
    )

if __name__ == "__main__":
    main()
