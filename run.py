from app import app
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    print(f"""
    ╔═══════════════════════════════════════╗
    ║     MAHESSA TRANS - RENTAL MOBIL      ║
    ╚═══════════════════════════════════════╝
    
    🚗 Server berjalan di: http://localhost:{port}
    🔧 Debug Mode: {'ON' if debug else 'OFF'}
    
    📱 Untuk mengakses dari device lain:
       http://[IP-ADDRESS]:{port}
    
    ⚠️  Press CTRL+C to quit
    ════════════════════════════════════════
    """)
    
    app.run(host='0.0.0.0', port=port, debug=debug)