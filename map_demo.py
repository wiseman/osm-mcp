#!/usr/bin/env python3
"""
Map Control Demo - Shows how to use the Flask server to control the map display
"""

import sys
import os
import time

# Set up the path to find our package
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from mcp_osm.flask_server import FlaskServer

def demo_map_controls():
    # Initialize and start the Flask server
    server = FlaskServer()
    server.start()
    
    print("Map server started. Open http://127.0.0.1:5000 in your browser.")
    print("This demo will show various map features after you open the page.")
    time.sleep(5)  # Give some time for the browser to connect
    
    # Example 1: Set the map title
    print("\nSetting map title...")
    server.set_title("San Francisco Landmarks", {"color": "#0066cc"})
    time.sleep(2)
    
    # Example 2: Set the map view
    print("\nSetting map view to San Francisco...")
    server.set_view(center=[37.7749, -122.4194], zoom=12)
    time.sleep(3)
    
    # Example 3: Show a marker
    print("\nAdding a marker at Coit Tower...")
    server.show_marker(
        coordinates=[37.8024, -122.4058],
        text="Coit Tower, San Francisco",
        options={"title": "Coit Tower"}
    )
    time.sleep(3)
    
    # Example 4: Show a polygon around Golden Gate Park
    print("\nAdding a polygon around Golden Gate Park...")
    golden_gate_park = [
        [37.7694, -122.5110],
        [37.7694, -122.4566],
        [37.7646, -122.4566],
        [37.7646, -122.5110]
    ]
    server.show_polygon(
        coordinates=golden_gate_park,
        options={"color": "green", "fillOpacity": 0.3}
    )
    time.sleep(3)
    
    # Example 5: Show a line for Market Street
    print("\nAdding a line along Market Street...")
    market_street = [
        [37.7944, -122.3953],  # Ferry Building
        [37.7932, -122.3967],
        [37.7909, -122.4013],
        [37.7891, -122.4051],
        [37.7865, -122.4113],  # Powell Street
        [37.7835, -122.4173],
        [37.7811, -122.4219]   # Civic Center
    ]
    server.show_line(
        coordinates=market_street,
        options={"color": "red", "weight": 5, "dashArray": "10,15"}
    )
    time.sleep(3)
    
    # Update the title with additional information
    print("\nUpdating map title with additional information...")
    server.set_title("San Francisco Landmarks - Golden Gate Park Area", 
                    {"color": "#006600", "backgroundColor": "rgba(255, 255, 255, 0.9)"})
    time.sleep(2)
    
    # Example 6: Get the current view
    print("\nCurrent map view:")
    current_view = server.get_current_view()
    print(f"  Center: {current_view['center']}")
    print(f"  Zoom: {current_view['zoom']}")
    if current_view['bounds']:
        print(f"  Bounds: {current_view['bounds']}")
    
    print("\nDemo complete! Keep the browser window open to interact with the map.")
    print("Press Ctrl+C to stop the server when you're done.")
    
    # Keep the script running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping server...")
        server.stop()
        print("Server stopped.")

if __name__ == "__main__":
    demo_map_controls() 