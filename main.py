import flet as ft


def main(page: ft.Page):
  page.title = "Silkscreen Xpress - BOM Calculator"
  page.scroll = ft.ScrollMode.AUTO
  page.theme_mode = ft.ThemeMode.LIGHT
  page.vertical_alignment = ft.MainAxisAlignment.START
  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

  # Header Title
  header = ft.Container(
      content=ft.Text(
          "BILL OF MATERIALS & COSTING SHEET",
          color=ft.colors.WHITE,
          weight=ft.FontWeight.BOLD,
          size=15,
          text_align="center",
      ),
      bgcolor=ft.colors.GREY_900,
      padding=12,
      alignment=ft.alignment.center,
      border_radius=8,
      width=580,
  )

  # Initial Data rows
  initial_items = [
      ("1", "#100 MESH", "METER", "1", "180"),
      ("2", "TABLE ADHESIVE", "KILO", "1", "270"),
      ("3", "100 ml BLACK PIGMENT", "ML", "1", "80"),
      ("4", "EMULSION", "KILO", "1", "560"),
      ("5", "SUPERWHITE", "KILO", "2", "285"),
      ("6", "SCREEN PREP", "PROJECT", "1", "1000"),
      ("7", "", "", "", ""),
      ("8", "", "", "", ""),
      ("9", "", "", "", ""),
      ("10", "", "", "", ""),
      ("11", "", "", "", ""),
      ("12", "", "", "", ""),
  ]

  item_inputs = []
  rows_controls = []

  # Table Headers
  header_row = ft.Row(
      [
          ft.Text("No.", weight=ft.FontWeight.BOLD, size=10, width=25),
          ft.Text(
              "Item Description", weight=ft.FontWeight.BOLD, size=10, width=150
          ),
          ft.Text("Unit", weight=ft.FontWeight.BOLD, size=10, width=60),
          ft.Text("Qty", weight=ft.FontWeight.BOLD, size=10, width=40),
          ft.Text("Unit Cost", weight=ft.FontWeight.BOLD, size=10, width=65),
          ft.Text("Total", weight=ft.FontWeight.BOLD, size=10, width=65),
          ft.Text("Total (15%)", weight=ft.FontWeight.BOLD, size=10, width=65),
      ],
      spacing=5,
  )


  # Helper para sa makapal na border ng text fields
  def styled_tf(val, w, align="left"):
    tf = ft.TextField(
        value=val,
        width=w,
        text_size=10,
        dense=True,
        text_align=align,
        border_color=ft.colors.OUTLINE,
        border_width=1.5,
        focused_border_width=2,
        border_radius=4,
        content_padding=5,
    )
    return tf


  # Dynamic rows generation
  for item_no, desc, unit, qty, cost in initial_items:
    no_lbl = ft.Text(item_no, size=10, width=25, text_align="center")
    desc_tf = styled_tf(desc, 150)
    unit_tf = styled_tf(unit, 60)
    qty_tf = styled_tf(qty, 40, "center")
    cost_tf = styled_tf(cost, 65, "right")

    tot_text = ft.Text("0.00", size=10, text_align="right")
    tot_container = ft.Container(
        content=tot_text,
        width=65,
        height=32,
        alignment=ft.alignment.center_right,
        padding=ft.padding.only(right=5),
        border=ft.border.all(1.5, ft.colors.OUTLINE),
        border_radius=4,
    )

    tot15_text = ft.Text("0.00", size=10, text_align="right")
    tot15_container = ft.Container(
        content=tot15_text,
        width=65,
        height=32,
        alignment=ft.alignment.center_right,
        padding=ft.padding.only(right=5),
        border=ft.border.all(1.5, ft.colors.OUTLINE),
        border_radius=4,
    )

    item_inputs.append({
        "qty": qty_tf,
        "cost": cost_tf,
        "desc": desc_tf,
        "unit": unit_tf,
        "tot": tot_text,
        "tot15": tot15_text,
    })

    rows_controls.append(
        ft.Row(
            [
                no_lbl,
                desc_tf,
                unit_tf,
                qty_tf,
                cost_tf,
                tot_container,
                tot15_container,
            ],
            spacing=5,
        )
    )

  # Subtotal Row na eksaktong naka-align gamit ang malinis na layout
  subtotal_tot_text = ft.Text(
      "0.00", size=10, weight=ft.FontWeight.BOLD, text_align="right"
  )
  subtotal_tot_container = ft.Container(
      content=subtotal_tot_text,
      width=65,
      height=32,
      alignment=ft.alignment.center_right,
      padding=ft.padding.only(right=5),
      border=ft.border.all(1.5, ft.colors.GREEN),
      border_radius=4,
      bgcolor=ft.colors.GREEN_50,
  )

  subtotal_tot15_text = ft.Text(
      "0.00", size=10, weight=ft.FontWeight.BOLD, text_align="right"
  )
  subtotal_tot15_container = ft.Container(
      content=subtotal_tot15_text,
      width=65,
      height=32,
      alignment=ft.alignment.center_right,
      padding=ft.padding.only(right=5),
      border=ft.border.all(1.5, ft.colors.GREEN),
      border_radius=4,
      bgcolor=ft.colors.GREEN_50,
  )

  # Ginawa nating eksaktong tugma ang width ng mga blangko/label sa itaas para sa perpektong alignment
  subtotal_row = ft.Row(
      [
          ft.Text("", width=25),  # Katumbas ng No. column
          ft.Text(
              "SUBTOTAL",
              weight=ft.FontWeight.BOLD,
              size=10,
              width=330,
              text_align="right",
          ),  # Sakop ang Description hanggang Unit Cost
          subtotal_tot_container,
          subtotal_tot15_container,
      ],
      spacing=5,
  )

  # Summary Inputs Section
  project_qty_tf = ft.TextField(
      label="Project Total Quantity (Pcs e.g. 200)",
      value="200",
      text_size=11,
      dense=True,
      border_width=1.5,
  )
  delivery_tf = ft.TextField(
      label="Delivery Fee (₱)",
      value="1000",
      text_size=11,
      dense=True,
      border_width=1.5,
  )
  labor_tf = ft.TextField(
      label="Installation / Labor Cost (₱)",
      value="3250",
      text_size=11,
      dense=True,
      border_width=1.5,
  )
  profit_tf = ft.TextField(
      label="Profit Margin (%)",
      value="100",
      text_size=11,
      dense=True,
      border_width=1.5,
  )

  # Result Display Box
  result_text = ft.Text(
      "I-click ang 'COMPUTE TOTALS' para sa summary.",
      size=11,
      color=ft.colors.WHITE,
      weight=ft.FontWeight.BOLD,
  )


  def calculate(e):
    try:
      sum_total = 0.0
      sum_total15 = 0.0

      for item in item_inputs:
        q_val = item["qty"].value.strip()
        c_val = item["cost"].value.strip()

        q = float(q_val) if q_val else 0.0
        c = float(c_val) if c_val else 0.0

        t = q * c
        t15 = t * 1.15

        item["tot"].value = f"{t:,.2f}" if t > 0 else "0.00"
        item["tot15"].value = f"{t15:,.2f}" if t15 > 0 else "0.00"

        sum_total += t
        sum_total15 += t15

      # Update Subtotal values sa baba ng table
      subtotal_tot_text.value = f"{sum_total:,.2f}"
      subtotal_tot15_text.value = f"{sum_total15:,.2f}"

      project_qty = float(project_qty_tf.value or 1)
      delivery = float(delivery_tf.value or 0)
      labor = float(labor_tf.value or 0)
      profit_pct = float(profit_tf.value or 0) / 100.0

      profit_amount = sum_total15 * profit_pct
      grand_total = sum_total15 + profit_amount + delivery + labor
      per_piece = grand_total / project_qty if project_qty > 0 else 0

      result_text.value = (
          f"Total Materials (Base): ₱{sum_total:,.2f}\n"
          f"Total w/ 15% Allowance: ₱{sum_total15:,.2f}\n"
          f"Profit ({int(profit_pct*100)}% of Material w/ 15%):"
          f" ₱{profit_amount:,.2f}\n"
          f"Delivery: ₱{delivery:,.2f}  |  Labor/Installation: ₱{labor:,.2f}\n"
          f"--------------------------------------------------\n"
          f"GRAND TOTAL QUOTATION: ₱{grand_total:,.2f}\n"
          f"PROJECT QTY: {int(project_qty)} pcs  |  PRICE / PC:"
          f" ₱{per_piece:,.2f}"
      )
      page.update()
    except ValueError:
      result_text.value = (
          "Error: Paki-siguro na puro numero ang Qty at Unit Cost."
      )
      page.update()


  compute_btn = ft.ElevatedButton(
      text="COMPUTE TOTALS",
      on_click=calculate,
      bgcolor=ft.colors.GREEN,
      color=ft.colors.WHITE,
  )

  main_content = ft.Column(
      [
          header,
          ft.Divider(height=10, color=ft.colors.TRANSPARENT),
          header_row,
          *rows_controls,
          subtotal_row,
          ft.Divider(),
          project_qty_tf,
          delivery_tf,
          labor_tf,
          profit_tf,
          ft.Divider(),
          ft.Row([compute_btn], alignment=ft.MainAxisAlignment.CENTER),
          ft.Container(
              content=result_text,
              bgcolor=ft.colors.GREY_900,
              padding=12,
              border_radius=8,
              margin=ft.margin.only(top=5, bottom=20),
              width=580,
          ),
      ],
      horizontal_alignment=ft.CrossAxisAlignment.CENTER,
      spacing=8,
  )

  page.add(
      ft.Container(content=main_content, padding=10, alignment=ft.alignment.center)
  )


ft.app(main)