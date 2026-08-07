import 'package:flutter/material.dart';

class WavyBackground extends StatelessWidget {
  final Widget child;

  const WavyBackground({super.key, required this.child});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFE8F1FC), // --bg-body
      body: Stack(
        children: [
          // Top Wave
          Positioned(
            top: -50,
            right: -50,
            child: Container(
              width: 200,
              height: 200,
              decoration: const BoxDecoration(
                color: Color(0xFFDCEAFB),
                borderRadius: BorderRadius.only(
                  topLeft: Radius.circular(80),
                  topRight: Radius.circular(120),
                  bottomLeft: Radius.circular(140),
                  bottomRight: Radius.circular(60),
                ),
              ),
            ),
          ),
          // Middle Wave
          Positioned(
            top: MediaQuery.of(context).size.height * 0.4,
            right: -80,
            child: Container(
              width: 250,
              height: 250,
              decoration: const BoxDecoration(
                color: Color(0xFFDCEAFB),
                shape: BoxShape.circle,
              ),
            ),
          ),
          // Bottom Wave
          Positioned(
            bottom: -50,
            right: -50,
            child: Opacity(
              opacity: 0.5,
              child: Container(
                width: 300,
                height: 300,
                decoration: const BoxDecoration(
                  color: Color(0xFFB9D9F8),
                  borderRadius: BorderRadius.only(
                    topLeft: Radius.circular(180),
                    topRight: Radius.circular(120),
                    bottomLeft: Radius.circular(90),
                    bottomRight: Radius.circular(210),
                  ),
                ),
              ),
            ),
          ),
          // Content
          SafeArea(
            child: child,
          ),
        ],
      ),
    );
  }
}
