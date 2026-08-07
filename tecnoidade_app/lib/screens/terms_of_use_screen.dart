import 'package:flutter/material.dart';
import '../widgets/wavy_background.dart';

class TermsOfUseScreen extends StatelessWidget {
  const TermsOfUseScreen({super.key});

  @override
  Widget build(BuildContext context) {
    const textColor = Color(0xFF333333);
    const primaryBlue = Color(0xFF3A45B8);
    const bgSection = Color(0xFFC6DDF6);
    const darkGray = Color(0xFF444444);

    return WavyBackground(
      child: SingleChildScrollView(
        padding: const EdgeInsets.symmetric(horizontal: 20.0, vertical: 20.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Header
            Row(
              children: [
                InkWell(
                  onTap: () => Navigator.of(context).pop(),
                  borderRadius: BorderRadius.circular(20),
                  child: Container(
                    width: 40,
                    height: 40,
                    decoration: const BoxDecoration(
                      color: Colors.white,
                      shape: BoxShape.circle,
                      boxShadow: [
                        BoxShadow(
                          color: Colors.black12,
                          blurRadius: 5,
                          offset: Offset(0, 2),
                        )
                      ],
                    ),
                    child: const Icon(
                      Icons.arrow_back_ios_new,
                      color: primaryBlue,
                      size: 20,
                    ),
                  ),
                ),
                const SizedBox(width: 15),
                const Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      'Termos de uso',
                      style: TextStyle(
                        fontSize: 24,
                        fontWeight: FontWeight.w800,
                        color: textColor,
                      ),
                    ),
                    Text(
                      'Tecnoidade versão 2.0',
                      style: TextStyle(
                        fontSize: 12,
                        fontWeight: FontWeight.w800,
                        color: Color(0xFF555555),
                      ),
                    ),
                  ],
                ),
              ],
            ),
            const SizedBox(height: 25),

            // Highlight Section
            Container(
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                color: bgSection,
                borderRadius: BorderRadius.circular(8),
              ),
              child: const Text(
                'Estes termos regem o uso da plataforma Tecnoidade. Ao utilizar nossos serviços, você concorda com as condições abaixo. Leia com atenção.',
                style: TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.w700,
                  color: textColor,
                  height: 1.5,
                ),
              ),
            ),
            const SizedBox(height: 25),

            // Policy Content
            const Text(
              'Termos de Uso – Aplicativo TecnoIdade',
              style: TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.w800,
                color: darkGray,
              ),
            ),
            const SizedBox(height: 10),
            const Text(
              'Última atualização: Julho de 2026',
              style: TextStyle(
                fontSize: 15,
                fontWeight: FontWeight.w800,
                color: darkGray,
              ),
            ),
            const SizedBox(height: 25),

            const Text(
              '1. Aceitação dos Termos',
              style: TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.w800,
                color: darkGray,
              ),
            ),
            const SizedBox(height: 15),
            const Text(
              'Bem-vindo ao TecnoIdade. Ao utilizar este aplicativo, o usuário declara que leu, compreendeu e concorda com os presentes Termos de Uso. Caso não concorde com qualquer condição aqui estabelecida, recomenda-se que não utilize o aplicativo.',
              style: TextStyle(
                fontSize: 15,
                fontWeight: FontWeight.w700,
                color: darkGray,
                height: 1.5,
              ),
            ),
            const SizedBox(height: 25),

            const Text(
              '2. Sobre o TecnoIdade',
              style: TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.w800,
                color: darkGray,
              ),
            ),
            const SizedBox(height: 15),
            const Text(
              'O TecnoIdade é uma plataforma educacional desenvolvida para promover a inclusão digital de pessoas idosas por meio de cursos, simulações, vídeos, atividades e materiais educativos sobre o uso de tecnologias no dia a dia.\n\nO aplicativo possui caráter exclusivamente educativo e não substitui orientações de instituições financeiras, órgãos públicos ou empresas responsáveis pelos serviços apresentados.',
              style: TextStyle(
                fontSize: 15,
                fontWeight: FontWeight.w700,
                color: darkGray,
                height: 1.5,
              ),
            ),
            const SizedBox(height: 25),

            const Text(
              '3. Cadastro e Acesso',
              style: TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.w800,
                color: darkGray,
              ),
            ),
            const SizedBox(height: 15),
            const Text(
              'Para utilizar determinadas funcionalidades, o usuário poderá realizar um cadastro fornecendo informações básicas, como nome, e-mail e senha.',
              style: TextStyle(
                fontSize: 15,
                fontWeight: FontWeight.w700,
                color: darkGray,
                height: 1.5,
              ),
            ),
            const SizedBox(height: 40),
          ],
        ),
      ),
    );
  }
}
