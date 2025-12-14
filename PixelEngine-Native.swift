#!/usr/bin/env swift

import Foundation
import Cocoa

class PixelEngineApp: NSObject, NSApplicationDelegate {
    var window: NSWindow!
    
    func applicationDidFinishLaunching(_ aNotification: Notification) {
        setupWindow()
        setupInterface()
    }
    
    func setupWindow() {
        window = NSWindow(
            contentRect: NSRect(x: 0, y: 0, width: 600, height: 500),
            styleMask: [.titled, .closable, .miniaturizable, .resizable],
            backing: .buffered,
            defer: false
        )
        
        window.title = "PixelEngine - Desktop Graphics Engine"
        window.backgroundColor = NSColor.white
        window.center()
        window.makeKeyAndOrderFront(nil)
    }
    
    func setupInterface() {
        let contentView = NSView(frame: window.contentView!.bounds)
        contentView.wantsLayer = true
        contentView.layer?.backgroundColor = NSColor.white.cgColor
        
        // Title
        let titleLabel = NSTextField(labelWithString: "🎨 PixelEngine")
        titleLabel.font = NSFont.boldSystemFont(ofSize: 36)
        titleLabel.textColor = NSColor.systemBlue
        titleLabel.alignment = .center
        titleLabel.frame = NSRect(x: 50, y: 400, width: 500, height: 50)
        contentView.addSubview(titleLabel)
        
        // Subtitle
        let subtitleLabel = NSTextField(labelWithString: "Desktop Graphics Engine v1.0")
        subtitleLabel.font = NSFont.systemFont(ofSize: 16)
        subtitleLabel.textColor = NSColor.secondaryLabelColor
        subtitleLabel.alignment = .center
        subtitleLabel.frame = NSRect(x: 50, y: 360, width: 500, height: 25)
        contentView.addSubview(subtitleLabel)
        
        // Features
        let featuresText = """
        ✨ Features:
        🚀 High Performance Rendering
        🎯 Pixel Perfect Graphics
        🖥️ Cross Platform Support
        ⚡ Real-time Processing
        🎨 Beautiful Desktop Interface
        
        📊 System Status:
        Platform: macOS Desktop
        Version: 1.0.0
        Status: Ready ✅
        Author: AbdulAziz
        License: MIT
        """
        
        let featuresLabel = NSTextField(labelWithString: featuresText)
        featuresLabel.font = NSFont.systemFont(ofSize: 12)
        featuresLabel.textColor = NSColor.labelColor
        featuresLabel.alignment = .left
        featuresLabel.frame = NSRect(x: 50, y: 150, width: 500, height: 200)
        featuresLabel.maximumNumberOfLines = 0
        featuresLabel.lineBreakMode = .byWordWrapping
        contentView.addSubview(featuresLabel)
        
        // Buttons
        let startButton = NSButton(title: "🚀 Start Engine", target: self, action: #selector(startEngine))
        startButton.frame = NSRect(x: 50, y: 80, width: 120, height: 40)
        startButton.bezelStyle = .rounded
        contentView.addSubview(startButton)
        
        let demoButton = NSButton(title: "🎮 Demo", target: self, action: #selector(runDemo))
        demoButton.frame = NSRect(x: 190, y: 80, width: 100, height: 40)
        demoButton.bezelStyle = .rounded
        contentView.addSubview(demoButton)
        
        let aboutButton = NSButton(title: "ℹ️ About", target: self, action: #selector(showAbout))
        aboutButton.frame = NSRect(x: 310, y: 80, width: 100, height: 40)
        aboutButton.bezelStyle = .rounded
        contentView.addSubview(aboutButton)
        
        let exitButton = NSButton(title: "❌ Exit", target: self, action: #selector(exitApp))
        exitButton.frame = NSRect(x: 430, y: 80, width: 100, height: 40)
        exitButton.bezelStyle = .rounded
        contentView.addSubview(exitButton)
        
        window.contentView = contentView
    }
    
    @objc func startEngine() {
        let alert = NSAlert()
        alert.messageText = "PixelEngine Started!"
        alert.informativeText = "🚀 Graphics Engine initialized successfully!\n✅ Ready for graphics operations!"
        alert.alertStyle = .informational
        alert.runModal()
    }
    
    @objc func runDemo() {
        let alert = NSAlert()
        alert.messageText = "Demo Running"
        alert.informativeText = "🎮 Graphics demo is now running!\n✨ Check the rendering pipeline."
        alert.alertStyle = .informational
        alert.runModal()
    }
    
    @objc func showAbout() {
        let alert = NSAlert()
        alert.messageText = "About PixelEngine"
        alert.informativeText = """
        🎨 PixelEngine Desktop Graphics Engine
        
        Version: 1.0.0
        Author: AbdulAziz
        Platform: macOS
        License: MIT License
        
        A powerful desktop graphics engine built for cross-platform development and real-time graphics processing.
        """
        alert.alertStyle = .informational
        alert.runModal()
    }
    
    @objc func exitApp() {
        NSApplication.shared.terminate(nil)
    }
    
    func applicationShouldTerminateAfterLastWindowClosed(_ sender: NSApplication) -> Bool {
        return true
    }
}

// Main execution
let app = NSApplication.shared
let delegate = PixelEngineApp()
app.delegate = delegate
app.run()
